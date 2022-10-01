async function firstTransaction() {

  try {
      let myAccount = createAccount();
      console.log("Press any key when the account is funded");
      await keypress();
      // Connect your client
      const algodToken = '2f3203f21e738a1de6110eba6984f9d03e5a95d7a577b34616854064cf2c0e7b';
      const algodServer = 'https://academy-algod.dev.aws.algodev.network/';
      const algodPort = '';
      let algodClient = new algosdk.Algodv2(algodToken, algodServer, algodPort);

      //Check your balance
      let accountInfo = await algodClient.accountInformation(myAccount.addr).do();
      console.log("Account balance: %d microAlgos", accountInfo.amount);
      let startingAmount = accountInfo.amount;
      // Construct the transaction
      let params = await algodClient.getTransactionParams().do();
      // comment out the next two lines to use suggested fee
      // params.fee = 1000;
      // params.flatFee = true;

      // receiver defined as TestNet faucet address 
      const receiver = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA";
      const enc = new TextEncoder();
      const note = enc.encode("Hello World");
      let amount = 100000;
      let closeout = receiver; //closeRemainderTo
      let sender = myAccount.addr;
      let txn = algosdk.makePaymentTxnWithSuggestedParams(sender, receiver, amount, closeout, note, params);
      // WARNING! all remaining funds in the sender account above will be sent to the closeRemainderTo Account 
      // In order to keep all remaning funds in the sender account after tx, set closeout parameter to undefined.
      // For more info see: 
      // https://developer.algorand.org/docs/reference/transactions/#payment-transaction

      // Sign the transaction
      let signedTxn = txn.signTxn(myAccount.sk);
      let txId = txn.txID().toString();
      console.log("Signed transaction with txID: %s", txId);

      // Submit the transaction
      await algodClient.sendRawTransaction(signedTxn).do();

      // Wait for confirmation
      let confirmedTxn = await algosdk.waitForConfirmation(algodClient, txId, 4);
      //Get the completed Transaction
      console.log("Transaction " + txId + " confirmed in round " + confirmedTxn["confirmed-round"]);
      var string = new TextDecoder().decode(confirmedTxn.txn.txn.note);
      console.log("Note field: ", string);
      accountInfo = await algodClient.accountInformation(myAccount.addr).do();
      console.log("Transaction Amount: %d microAlgos", confirmedTxn.txn.txn.amt);        
      console.log("Transaction Fee: %d microAlgos", confirmedTxn.txn.txn.fee);
      let closeoutamt = startingAmount - confirmedTxn.txn.txn.amt - confirmedTxn.txn.txn.fee;     
      console.log("Close To Amount: %d microAlgos", closeoutamt);
      console.log("Account balance: %d microAlgos", accountInfo.amount);
  }
  catch (err) {
      console.log("err", err);
  }
  process.exit();
};

firstTransaction();
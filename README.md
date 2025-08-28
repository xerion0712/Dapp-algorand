# End-to-End Web3 dApp: Algorand NFTs and Smart Contracts

## Introduction
Web3 is defined as a multi-layer architecture that leverages decentralized protocols and distributed technologies to provide a trusted application framework. At the core of this stack is a decentralized ledger system  that enables consensus-based, tamper-proof data management. This architecture integrates several core components: programmable smart contracts that automate deterministic logic, NFTs for representing unique digital assets, decentralized storage mechanisms like IPFS for resilient data distribution, blockchain-based oracles for secure external data provisioning, and crypto wallets for user controlled identity and asset management. This composable technology stack is designed to support powerful, permissionless applications that operate independently of central authorities.

## Project Objective
The project addresses the limitations of distributing certificates as static PDF files. The aim is to deliver certificates as digital assets (NFTs) on the Algorand blockchain, supporting on-chain verification, security, and additional functionality through smart contracts.[1]

## Development Environment

### Algorand Sandbox (Testnet)
Algorand offers a Docker-based sandbox for node setup and rapid development.  

```bash
git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up testnet
./sandbox up testnet -v
```

### Python SDK Installation
The Algorand Python SDK is available via pip.  

```bash
pip3 install py-algorand-sdk
```
Instructions for account creation are provided at the official Algorand developer documentation.

### React Application Setup
The sample implementation utilizes a React frontend available from an open-source repository:

```bash
git clone https://github.com/BirhanuGebisa/Algorand-dapps_smart-contract.git
cd algorand-NFTs-smartContracts
npm start
```
Access the local deployment at `http://localhost:8080`.

### Application Scripts
- `npm test` initiates the interactive test runner.
- `npm run build` optimizes the React application for production output.

### Backend Deployment
Use Flask to run the backend logic:

```bash
flask run
```

A deployment instance is available at:
https://lgorand-dapps-smart-contract.herokuapp.com/login

## Author
dev.xerion@gmail.com

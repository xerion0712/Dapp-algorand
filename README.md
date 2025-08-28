# End-to-End Web3 dApp: Algorand NFTs and Smart Contracts

## Introduction
Web3 refers to a framework built on decentralized protocols and technologies. This stack enables applications that are centered on user control and distributed consensus. Core components of Web3 include blockchains, smart contracts, non-fungible tokens (NFTs), decentralized storage networks, oracles, and crypto wallets.

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

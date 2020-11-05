# Coffee Shop Frontend

## Getting Setup

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, make sure you have them installed from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

#### Installing project dependencies

After cloning, and in the `frontend` directory, open your terminal and run:

```
npm install
```

### Configure Enviornment Variables

Ionic uses a configuration file to manage environment variables. These variables ship with the transpiled software and should not include secrets.

this frontend is designed to work with Flask-based [Backend](../backend).

- Open `./src/environments/environments.ts` and ensure each variable reflects the backend and your auth0 setup.

## Running the Frontend

To run the development server, run:

```
ionic serve
```

> _tip_: Do not use **ionic serve** in production. Instead, build Ionic into a build artifact for your desired platforms.
> [Checkout the Ionic docs to learn more](https://ionicframework.com/docs/cli/commands/build)

# ProgressArc

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

## Running the Backend

At the project directory, create and activate a virtual environment:

- For Windows,

```sh
python -m venv .venv
.venv/Scripts/activate
```

- For MacOS/Linux,

```sh
python -m venv .venv
source .venv/bin/activate
```

Then, install the required Python dependencies:

```sh
pip install -r requirements.txt
```

Finally, run the `auth-service` microservice:

```sh
python backend/auth-service/auth.py
```

A development Flask server will start at port 5000.

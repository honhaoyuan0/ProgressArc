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

1. At the project directory, create and activate a virtual environment:

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

2. Install the required Python dependencies:

```sh
pip install -r requirements.txt
```

3. Beg the developers to give you the necessary secrets, then put them in a `.env` file in the project root:

```
MONGO_URI=<SECRET>
FLASK_SECRET_KEY=<SECRET>
```

4. Run the `auth-service` microservice:

```sh
cd backend
flask --app auth_service/auth.py --debug run
```

A development Flask server will start at port 5000.

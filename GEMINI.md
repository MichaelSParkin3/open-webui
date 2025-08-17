# Open WebUI Project Overview

Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various Large Language Model (LLM) runners like Ollama and OpenAI-compatible APIs, with a built-in inference engine for Retrieval Augmented Generation (RAG). The project aims to provide a powerful and highly configurable AI deployment solution with a focus on user experience and extensibility.

## Technologies Used

*   **Frontend:** SvelteKit, Vite, TypeScript, Tailwind CSS. It utilizes Pyodide for in-browser Python execution, and various libraries for rich text editing, code highlighting, and real-time communication.
*   **Backend:** Python with FastAPI and Uvicorn. It supports multiple database backends (PostgreSQL, MySQL, MongoDB) using SQLAlchemy, Alembic, and Peewee. The backend integrates with numerous AI/LLM libraries (LangChain, Hugging Face Transformers, OpenAI, Anthropic, Google GenAI), document processing tools, and vector databases (ChromaDB, Milvus, Qdrant, Pinecone, OpenSearch) for its RAG capabilities. Real-time communication is handled via Socket.IO.
*   **Containerization & Deployment:** Docker, Docker Compose, Kubernetes (Kustomize, Helm).

## Building and Running

The project offers several methods for building, running, and deploying the application.

### Frontend Development

To run the frontend in development mode:
```bash
npm run dev
```
This will typically start the development server on `http://localhost:5173` (or another port if configured).

To build the frontend for production:
```bash
npm run build
```

### Python Pip Installation (Backend & Frontend)

If you prefer a direct Python installation:
1.  **Install Open WebUI:**
    ```bash
    pip install open-webui
    ```
2.  **Run Open WebUI:**
    ```bash
    open-webui serve
    ```
    This will start the server, accessible at `http://localhost:8080`.

### Docker

The primary and recommended way to run Open WebUI is via Docker.

**Using `run.sh` (simple Docker build and run):**
```bash
./run.sh
```
This script builds the Docker image and runs a container, mapping host port 3000 to container port 8080, and setting up data persistence.

**Using `docker-compose.yaml` (with Ollama):**
The `docker-compose.yaml` file defines a multi-service setup including both Open WebUI and Ollama.

*   **Start services (build if necessary):**
    ```bash
    docker compose up -d --build
    ```
*   **Start services (without rebuilding):**
    ```bash
    docker compose up -d
    ```
*   **Stop services:**
    ```bash
    docker compose stop
    ```
*   **Update services (pulls latest git, updates Ollama models, rebuilds):**
    ```bash
    make update
    ```

**Specific Docker `run` commands (from `README.md`):**
*   **Default (Ollama on host):**
    ```bash
    docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```
*   **With Nvidia GPU support:**
    ```bash
    docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
    ```
*   **Bundled Ollama (with GPU):**
    ```bash
    docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
    ```

### Kubernetes

Open WebUI can be deployed to Kubernetes using Kustomize or Helm.

*   **Kustomize (CPU-only):**
    ```bash
    kubectl apply -f ./kubernetes/manifest/base
    ```
*   **Kustomize (GPU-enabled):**
    ```bash
    kubectl apply -k ./kubernetes/manifest
    ```
*   **Helm (package first):**
    ```bash
    helm package ./kubernetes/helm/
    ```
*   **Helm (CPU-only):**
    ```bash
    helm install ollama-webui ./ollama-webui-*.tgz
    ```
*   **Helm (GPU-enabled):**
    ```bash
    helm install ollama-webui ./ollama-webui-*.tgz --set ollama.resources.limits.nvidia.com/gpu="1"
    ```

## Development Conventions

*   **Code Formatting:** The project enforces code formatting using Prettier for frontend files (`.js`, `.ts`, `.svelte`, `.css`, `.md`, `.html`, `.json`) and Black for Python backend files.
    *   `npm run format` (frontend)
    *   `npm run format:backend` (backend)
*   **Linting:** ESLint is used for frontend linting, and Pylint for backend linting.
    *   `npm run lint` (runs both frontend and backend linting)
    *   `npm run lint:frontend`
    *   `npm run lint:backend`
*   **Type Checking:** TypeScript is used for type safety in the frontend, checked with `svelte-check`.
    *   `npm run check`
*   **Testing:**
    *   **Frontend Unit Tests:** Vitest (`npm run test:frontend`).
    *   **End-to-End (E2E) Tests:** Cypress (`npm run cy:open`).
*   **Internationalization (i18n):** The project supports multiple languages, with tools like `i18next` and `i18next-parser`.
    *   `npm run i18n:parse`
*   **Extensibility:** The architecture supports plugins and pipelines, allowing for custom logic and integrations.
*   **Continuous Integration/Continuous Deployment (CI/CD):** GitHub Actions workflows are used for automated builds, linting, and deployments.

## Engineering Guidelines (MCPs)

**Git Commit Guidelines**

* Use Conventional Commits formatting.
* Use a prefix-based branch naming convention.
* Do **not** add the model as a co-author or include links to Claude Code.

**Visual Development Memories**

* Use the **Playwright MCP server** when making visual/front-end changes to check your work.

**Guidance Memories**

* Ask for clarification *up front* when the initial prompt lacks direction.

**Linting & Code Quality**

* Run `npm run lint` after large additions/refactors to maintain best practices.

**CLI Tooling Memories**

* Use the `gh` CLI where appropriate to create issues, open PRs, read comments, etc.

**Documentation Memories**

* Use **context7** to find relevant, up-to-date docs when working with third-party libraries, packages, or frameworks.

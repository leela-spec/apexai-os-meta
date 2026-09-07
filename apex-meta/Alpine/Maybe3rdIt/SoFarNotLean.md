### Why Does the Stack Consume So Much RAM When "Idle"?

Your intuition is completely natural. When we think of "containers," we often imagine tiny, lightweight processes. However, what is running here is **not** a set of simple lightweight utilities—it is **three complete enterprise-grade server platforms plus an enterprise database engine**:

1. **OpenProject (The Heaviest Consumer — ~1.8 to 2.5 GB at cold boot):**
    - OpenProject is a massive Ruby on Rails platform (similar in scale to GitLab or Redmine).
    - When it boots, it pre-loads hundreds of Ruby gems, pre-compiles assets, starts the **Puma** web server, and spins up **GoodJob** (the background task runner) with **20 concurrent worker threads and 16 background cron jobs**.
    - It immediately opens a pool of **17 persistent connection processes** into PostgreSQL.
    - _All of this happens at idle before you even log in._
2. **Paperless-ngx (~800 MB to 1.2 GB at idle):**
    - A full Python/Django application running Gunicorn, Celery asynchronous workers, a scheduler, and pre-loading heavy document-processing libraries (Tesseract OCR, PyMuPDF).
3. **PostgreSQL 16 + pgvector (~400 to 600 MB):**
    - Allocates shared memory buffers and forks a dedicated backend process for _each_ client connection (17 for OpenProject, plus connections for Paperless and Firefly).
4. **Firefly III, Hermes Agent, Valkey, Nginx (~500 MB combined):**
    - PHP/Laravel, Python 3.13 API daemon, Redis/Valkey cache, and Nginx.

**The Reality:**  
To simply exist in memory and listen on their ports without doing active work, these 7 enterprise runtimes require **at least 3.5 to 4.5 GB of actual physical RAM**.

Because Docker Desktop was restricted to a hard **2 GB ceiling**, 4.5 GB of active code and connection pools could not fit. The VM immediately filled its 1 GB swap file to **99.98%**, started killing OpenProject with Out-Of-Memory errors (`exit code 137`), and thrashed your laptop's SSD at **1.81 GB per second**, causing Windows to freeze.
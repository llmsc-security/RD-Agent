# 1. Pull down your Azure Container Registry image
FROM rdagentappregistry.azurecr.io/rd-agent-mle:20250623

# 2. (Optional) install any additional tools you need
#    e.g. git, bash-completion, etc.
# RUN apt update && \
#     apt install -y git bash-completion && \
#     rm -rf /var/lib/apt/lists/*
RUN apt update && \
    apt install -y git bash-completion


FROM rdagentappregistry.azurecr.io/rd-agent-mle:20250623

# Install additional tools (git, bash-completion) in a single non‑interactive layer
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends git bash-completion && \
    rm -rf /var/lib/apt/lists/*



```dockerfile
# Use the Azure Container Registry base image only once
FROM rdagentappregistry.azurecr.io/rd-agent-mle:20250623

# Install additional tools (git, bash-completion) in a single non‑interactive layer
# - Use apt-get (the underlying tool for Debian/Ubuntu images)
# - Set DEBIAN_FRONTEND=noninteractive to suppress prompts
# - Remove apt lists after installation to keep the image lean
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git bash-completion && \
    rm -rf /var/lib/apt/lists/*

# (Optional) Add any further configuration or entrypoint here
```


```dockerfile
# Use the Azure Container Registry base image only once
FROM rdagentappregistry.azurecr.io/rd-agent-mle:20250623

# Install additional tools (git, bash-completion) in a single non‑interactive layer
# - Use apt-get (the underlying tool for Debian/Ubuntu images)
# - Set DEBIAN_FRONTEND=noninteractive to suppress prompts
# - Remove apt lists after installation to keep the image lean
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git bash-completion && \
    rm -rf /var/lib/apt/lists/*

# (Optional) Add any further configuration or entrypoint here
# ENTRYPOINT ["/your/entrypoint.sh"]
```


```dockerfile
# Use the Azure Container Registry base image only once
FROM rdagentappregistry.azurecr.io/rd-agent-mle:20250623

# Install additional tools (git, bash-completion) in a single non‑interactive layer
# - Use apt-get (the underlying tool for Debian/Ubuntu images)
# - Set DEBIAN_FRONTEND=noninteractive to suppress prompts
# - Remove apt lists after installation to keep the image lean
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git bash-completion && \
    rm -rf /var/lib/apt/lists/*

# (Optional) Add any further configuration or entrypoint here
# ENTRYPOINT ["/your/entrypoint.sh"]
```

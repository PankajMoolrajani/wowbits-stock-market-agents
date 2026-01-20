# wowbits-stock-market-agents

A collection of AI agents for stock market analysis and monitoring built with the wowbits framework.

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

### 1. Install wowbits CLI

Install the wowbits command-line interface tool:
```
pip install --extra-index-url https://test.pypi.org/simple/ wowbits-cli==0.1.5
```

### 2. Install local dependencies to run functions
```
pip install -r functions/requirements.txt
```

### 3. Setup the env
```
wowbits setup
```

### 4. Create agent (optional)
```
wowbits create agent <agent-name> (agent name should be same as the yaml file under agents/<agent-name.yaml>
```

### 4. Run agent
```
wowbits run agent <agent-name>
wowbits run agent stock_news_monitor
```

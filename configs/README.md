# Configuration

The notebook defines its runtime configuration in code. These JSON files expose the public release settings for review and external tooling.

- `model_config.full.json`: 1,000-agent release configuration.
- `model_config.pilot.json`: 200-agent validation configuration.
- `llm_config.example.json`: non-secret LLM protocol settings.

The notebook remains authoritative until configuration loading is fully refactored into modules. Never store `ANTHROPIC_API_KEY` in these files.

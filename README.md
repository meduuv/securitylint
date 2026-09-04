# SecurityLint

> Static checks for common insecure configuration patterns.

SecurityLint is a lightweight defensive analysis tool that flags configuration patterns worth reviewing before they become security problems.

## Checks

- Wildcard bind addresses
- Credential-like configuration keys
- Debug mode enabled in configuration
- Missing secure-transport indicators
- Clear, actionable findings

The tool reports patterns. It does not modify the systems or configuration it analyzes.

## Workflow

```text
configuration
      ↓
static inspection
      ↓
findings
      ↓
review
      ↓
remediation
```

## Example

```bash
securitylint ./config.json
```

For the exact command-line interface and supported formats, see the installed package and tests.

## Why it exists

Many security problems start as ordinary configuration mistakes. A small static check can catch obvious risky patterns early without requiring a live target or intrusive testing.

## Safety

SecurityLint is intended for defensive code and configuration review. It does not perform exploitation, credential collection or unauthorized access.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu
# analyze-auth0

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for `tap-auth0`. These datasets are automatically added to your Matatika workspace when you initialize a `tap-auth0` pipeline.

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-auth0
  namespace: tap_auth0
  repo: https://github.com/Matatika/analyze-auth0.git
  pip_url: git+https://github.com/Matatika/analyze-auth0.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-auth0

# Add the file bundle as a related plugin through adding the Auth0 extractor
meltano add extractor --include-related tap-auth0
```

### Adding this along with tap-auth0 as a custom plug-in for in Matatika

Go to data imports, click on `Custom Data Source` and copy and paste in:

```yaml
extractors:
  - name: tap-auth0
    namespace: tap_auth0
    pip_url: git+https://github.com/Matatika/tap-auth0.git
    capabilities:
      - state
      - discover
      - catalog
    settings:
      - name: client_id
        kind: password
      - name: client_secret
        kind: password
      - name: domain
files:
  - name: analyze-auth0
    namespace: tap_auth0
    update:
      analyze/datasets/tap-auth0: true
    pip_url: git+https://github.com/Matatika/analyze-auth0.git
```
# infrahub-transform

This repo contains python transform, query and artifact defintions.
They can be used by Infrahub to create artifacts wihic will run a Kriten job.

## Testing

Set env vars to connect to infrahub:
```
export INFRAHUB_ADDRESS="http://192.168.10.57:8000"
export INFRAHUB_API_TOKEN="06438eb2-8019-4776-878c-0941b1f1d1ec"
source venv/bin/activate
```

Run infrahubctl:
```
infrahubctl transform switch_check_transform id="1875c944-b74a-8267-2d7c-c51385b22eb6"
```


## Instructions

Make sure the object that contains the artifact inherits from CoreArtifactTarget (See schema.yml)

Add a standard group in Infrahub -> Object Management > Groups
Group name must match "targets" in artifact definition in .infrahub.yml
Add switches as members of the group

Add this repository in Infrahub -> Integrations > Git Repositories

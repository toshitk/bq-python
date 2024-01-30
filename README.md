# gcloud CLI
## Initializing
`gcloud init`

## Set configuration
If there is an existing configuration, switch config
- `gcloud config configurations list`
```
NAME        IS_ACTIVE  ACCOUNT            PROJECT              COMPUTE_DEFAULT_ZONE  COMPUTE_DEFAULT_REGION
default     False      email@example.com  default-project
configA     True       email@example.com  sample-project
```
- `gcloud config configurations activate <CONFIG NAME>`

## Set project
`gcloud projects list`
```
PROJECT_ID      NAME     PROJECT_NUMBER
aaa-aaa-123456  Project  123456789012
bbb-bbb-123456  Project  210987654321
```
`gcloud config set project <PROJECT ID>`

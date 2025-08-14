I use this repository to test features and improvements related to https://github.com/machulav/ec2-github-runner

GH Actions secrets I have [set](https://github.com/ktdreyer/ec2-runner-test/settings/secrets/actions):

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
GH_PERSONAL_ACCESS_TOKEN
```

# GH_PERSONAL_ACCESS_TOKEN

Create a [new GitHub personal access token](https://github.com/settings/tokens). The upstream repository says to use the `repo` scope, and this refers to GitHub's "classic" tokens.

I'm testing using GitHub's newer fine-grained tokens, so that I can use modern security options, restrict this token to this single repo, and possibly even update the upstream documentation to use this...

With experimentation and reading [this in-progress PR](https://github.com/machulav/ec2-github-runner/pull/239), I've found that the token needs:

* Administration: read/write
* Metadata: read-only
* Contents: read-only

Once that PR is merged, we won't need the full `Administration` privilege when we use the GH Action within organizations.

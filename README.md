# GitHub Discussions API 

The GitHub discussions API for `ramptix/preprompted-data`.

## /body

```http
GET https://github-discussions-api.vercel.app/body?url=<URL>
```

Get a discussion body.

**Query Parameters**
- `url`: The discussion URL. (e.g., `https://github.com/ramptix/preprompted-data/discussions/2`)

**Response**
```json
{
  "body": "string"
}
```

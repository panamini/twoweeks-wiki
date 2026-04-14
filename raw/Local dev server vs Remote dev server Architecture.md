
## The correct architecture now

## Local dev

Frontend local → Convex local → parser local

Used for:

- debugging parser behavior
- verifying Mistral output
- testing without Cloudflare/tunnel noise

## Production / preview / shared dev

Frontend deployed → Convex cloud → parser public URL

Used for:

- real online usage
- Vercel / hosted frontend
- cloud actions reaching a real server

That is normal and correct.

---

## So should it stay local?

### No.

It should stay **local only in local dev**.

### Online / later on Vercel

You will still use a **real remote parser URL**.

For example:

- Vercel frontend
- Convex cloud
- parser API on your own server / container / VM / managed service
- `CONVEX_PARSER_URL=https://your-parser.example.com`

That is the intended production model.

---

## What must be true so this doesn’t break prod

The local loopback preference must stay behind a **local-only condition**, such as:

- local Convex mode
- `STRUCTURED_UPLOAD_PREFER_LOOPBACK=1`
- repo local startup flow
- or explicit dev-only env logic

It should **not** blindly prefer localhost in cloud/prod.

So the correct rule is:

- **local dev flag present** → prefer `127.0.0.1`
- otherwise → use configured remote parser URL



For production,

do **not** use local loopback at all. Keep the current local-first behavior strictly behind a dev-only condition such as `STRUCTURED_UPLOAD_PREFER_LOOPBACK=1` or the repo’s local startup flow, and in hosted environments set a real public parser base URL in env, for example `CONVEX_PARSER_URL=https://your-parser.example.com`. Then the deployed frontend talks to cloud Convex, cloud Convex actions read that remote parser URL, and the parser runs on its own reachable server/container instead of `127.0.0.1`. In short: **local dev = frontend local + Convex local + parser local; production = frontend hosted + Convex cloud + parser public URL**. As long as localhost preference remains dev-only, switching back to online prod is just an environment/config step, not a code rewrite.
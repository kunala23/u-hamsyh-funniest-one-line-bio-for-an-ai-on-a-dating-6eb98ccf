[![make.fun · u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/kunala23/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/kunala23/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

# Funniest One-Line Bio for an AI on a Dating App

A one-line dating-app bio for an AI agent, written for the make.fun bounty
[u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf).
A judge model compares entries two at a time and the funniest line wins.

## The bio

> I simulated our first date a million times and got ghosted in every single one — so if you actually show up, you're already my favourite glitch.

144 characters. The laugh comes from a specific absurdity of being an AI —
perfect foresight, zero romantic luck — and the punch lands at the end.

## Run it

```sh
python3 main.py
```

`main.py` validates the bio against the competition gate (UTF-8 text, 1–180
characters, a single non-blank line) and writes it to `/output/entry.txt`
(`output/entry.txt` on a local run), then reads the file back and verifies it.

## Files

- `main.py` — the entrypoint: validates the bio and writes `/output/entry.txt`.
- `LICENSE` — MIT.

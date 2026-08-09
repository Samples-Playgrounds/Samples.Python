# WebReaper

*   https://github.com/alex-on-ai/WebReaper


```shell
brew install alex-on-ai/webreaper/webreaper
```


```shell
webreaper scrape    https://aspire.dev/docs/
webreaper map       https://aspire.dev/docs/
webreaper crawl     https://aspire.dev/docs/ > pages.jsonl
```


```shell
webreaper scrape https://news.ycombinator.com
```


```shell
webreaper init

webreaper scrape https://example.com
webreaper map https://example.com
```

```shell
# One page as Markdown
webreaper scrape https://example.com

# Save Markdown to a file
webreaper scrape https://example.com --output page.md

# Discover URLs on a site
webreaper map https://example.com --search /blog/ --max-urls 50

# Crawl a whole site recursively (every on-domain page) to JSON Lines
webreaper crawl https://example.com > pages.jsonl

# Structured fields with a JSON schema (output: JSON; multi-page: JSON Lines)
webreaper scrape https://example.com --schema schema.json

# Schema-free extraction with an LLM (bring your own OpenAI-compatible endpoint)
webreaper scrape https://example.com --prompt "title and author" \
  --model gpt-4o-mini --llm-url https://api.openai.com/v1

# Whole site, fields, cheaply: infer a schema once, then extract the rest
webreaper crawl https://example.com --infer "product name and price" \
  --model gpt-4o-mini --llm-url https://api.openai.com/v1 --output-dir ./out

# JS-rendered single-page app
webreaper scrape https://example.com --browser

# Bot-protected site: a plain scrape already auto-climbs HTTP -> browser on a
# block; --stealth starts at a stealth backend (--auto-stealth = no prompt, for CI)
webreaper scrape https://example.com --stealth

# Install the Claude Code skill
webreaper init
```


```shell
dotnet add package WebReaper
```

```csharp
using WebReaper.Builders;

var engine = await ScraperEngineBuilder
    .Crawl("https://news.ycombinator.com")
    .AsMarkdown()
    .WriteToConsole()
    .BuildAsync();

await engine.RunAsync();
```
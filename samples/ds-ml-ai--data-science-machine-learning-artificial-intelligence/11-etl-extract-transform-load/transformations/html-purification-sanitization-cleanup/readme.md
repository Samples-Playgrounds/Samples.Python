# HTML transformations

## Cleaup Purification

*   https://github.com/PixxxeL/python-html-purifier

*   https://lxml.de/api/lxml.html.clean.Cleaner-class.html

### Styles

*   https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_remove_all_styles.htm

### Scripts

*   https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_remove_all_scripts.htm


## Diverse

*   https://stackoverflow.com/questions/3073881/clean-up-html-in-python

http://codespeak.net/lxml/lxmlhtml.html#cleaning-up-html


Bleach
Strengths: Widely used, actively maintained, battle-tested, simple API (clean, linkify), good defaults that prioritize safety, integrates with html5lib parser.
Controls: allowlists for tags, attributes, styles; protocols; strip or escape disallowed content.
Use when: you need a secure, easy-to-use sanitizer for user-submitted HTML, comments, WYSIWYG output, or Markdown-to-HTML pipelines.
Notes: Performance is adequate for typical web apps; extensible but not designed for complex policy engines.
html-sanitizer (also known as python-html-sanitizer by mozilla? / often html5lib-sanitizer variants)
Strengths: Strict, small, focuses on correctness and adherence to HTML parsing rules; conservative defaults.
Controls: fine-grained policies, canonicalization via html5lib.
Use when: strict normalization and minimal attack surface matter; projects preferring tiny dependency surface.
Notes: Less widely adopted than Bleach.
defusedxml / lxml’s cleaner
Strengths: lxml.html.clean.Cleaner is fast and featureful (remove scripts, styles, comments, dangerous attributes), can operate on parsed trees, configurable.
Controls: allowlists, strip or drop elements, keep CSS classes, safe attributes options.
Use when: performance matters, you already use lxml for parsing/manipulation, or need to clean large documents.
Notes: lxml is a C extension (platform dependency). Be careful with XML-specific attack vectors; combine with safe parsing.


Sanitizer built on html5lib’s treebuilder
Strengths: canonical HTML5 parsing behavior, robust against malformed HTML.
Use when: you want parsing correctness first and will layer sanitization policy on top.
DOMPurify (via Pyodide / JS embedding or server-side JS)
Strengths: de facto standard in browser/JS world; extremely robust and actively maintained.
Use when: you can run a tiny JS runtime (Node/Pyodide) or want parity with client-side sanitization.
Notes: Not pure Python; useful when absolute feature parity with browser sanitizer is required.
Recommendation matrix (practical):

Best general-purpose, secure, and easiest to adopt: Bleach.
Best for high-performance server-side cleaning when already using lxml: lxml.html.clean.Cleaner.
Best minimalist/strict policy: python-html-sanitizer / html-sanitizer.
Best for parity with browser behavior: DOMPurify (via Node or WASM) if using JS runtime is acceptable.
Practical guidance and pitfalls

Prefer allowlist (whitelist) over blacklist. Only permit specific tags, attributes and URL protocols.
Canonicalize input before checking protocols/attributes (use html5lib or equivalent) to avoid bypasses via encoded or malformed content.
Strip or neutralize dangerous attributes: event handlers (on*), javascript: URIs, data: URIs (or restrict data: to known safe types).
Carefully handle CSS: inline styles can carry dangerous expressions; either strip style attributes or use a CSS sanitizer library to allow only safe properties and values.
Keep libraries updated; sanitizer vulnerabilities and bypasses are periodically discovered.
When client and server both sanitize, ensure policies align to avoid surprises (e.g., server strips something the client shows).
Test with common adversarial payloads (javascript: URIs, SVG with script, malformed tags, character encodings).
Example quick choices by scenario

Typical web app/comments/WYSIWYG: Bleach with a conservative tag/attribute list.
High-throughput HTML processing and you already use lxml: lxml Cleaner + well-defined allowlist.
Need absolute HTML5 parsing correctness and canonicalization: html5lib + a policy layer (or html-sanitizer).
Need browser-equivalent sanitization: run DOMPurify in Node or WASM.
Summary

For most Python projects the pragmatic choice is Bleach — it offers a secure default configuration, easy customization, and wide adoption. For specialized needs (performance, strictness, or browser parity), consider lxml Cleaner, html-sanitizer, or DOMPurify (via a JS runtime). Follow allowlist principles, canonicalize input, and test with real attack vectors.


Sanitize-html provides a simple HTML sanitizer with a clear API.

Sanitize-html is tolerant. It is well suited for cleaning up HTML fragments such as those created by CKEditor and other rich text editors. It is especially handy for removing unwanted CSS when copying and pasting from Word.

Sanitize-html allows you to specify the tags you want to permit, and the permitted attributes for each of those tags.



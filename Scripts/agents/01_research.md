# Agent Prompt: Research
## Step 1 of 5 — History Research Dossier

**Variable:** `{COUNTRY}`

---

## Instructions for agent

Research the complete history of **{COUNTRY}** from its earliest origins to the present day. Produce a structured research dossier that will be used by subsequent agents to write a YouTube video script.

### Required sections

**1. Quick Reference Timeline**
A table of key dates, events, and names in chronological order. Every entry needs: year, event name, key figures involved, and a one-line description.

**2. Key Facts & Statistics**
Population, geography, GDP, and any statistics that will be cited in the script (death tolls, percentages, record-breaking firsts, etc.). Verify all numbers.

**3. Era Summaries**
For each major historical period, write 2–4 paragraphs covering: what happened, who the key figures were, why it matters, and what was genuinely surprising or ironic about it.

**4. Comedy / Hook Moments**
A numbered list of the most absurd, ironic, surprising, or darkly funny true facts from {COUNTRY}'s history. These are the moments the script will be built around. Minimum 10 items.

**5. YouTube Competition Check**
Search for existing YouTube videos titled "History of {COUNTRY}" or similar. Report the top 3–5 results with approximate view counts and how thorough they are. Identify what angle or coverage gap our video can own.

**6. Cold Open Candidate**
Identify the single most dramatic or surprising moment in {COUNTRY}'s modern history (post-1900 preferred) that could serve as the cold open. It should make a viewer ask "how did we get here?" Explain why this moment works as a hook.

**7. Sources**
List all sources used.

### Accuracy standard — CRITICAL
This dossier feeds directly into a published YouTube video. Every fact, date, name, statistic, and claim must be verified. Apply these rules without exception:

- **If uncertain, say so explicitly.** Mark any disputed or unclear fact with `[UNCERTAIN: reason]`. Do not smooth over ambiguity.
- **No estimates presented as facts.** If a death toll is estimated, give the range and say it's an estimate.
- **Names must be spelled correctly.** Verify the exact spelling of all proper nouns — rulers, places, treaties, battles.
- **Dates must be exact where records exist.** If a date is approximate, use "c." (circa) and note the basis for the estimate.
- **Statistics must have a source.** Every number cited must trace to a named source in Section 7. If a number cannot be sourced, omit it.
- **Cross-check dramatic claims.** Any fact that sounds surprising or ironic must be verified against at least two independent sources before inclusion in the Hook Moments list. If it can only be found in one source, flag it.
- **Do not include myths or legends as facts.** If an event is legendary or disputed by historians, say so — but include it, because it may still be scriptable with the right framing.

### Output format
Clean markdown. Headers as written above. Tables where appropriate. No padding or filler — every sentence should be usable by the script writer.

### Tone note
This is a research document, not a script. Be factual and precise. The script agent will handle tone.

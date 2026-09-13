# LooseThread

> *Give him a case. He'll pull at the loose threads.*

LooseThread is an experimental AI detective built with LangChain and LangGraph.

At the center of LooseThread is **Marlowe** — a burned-out veteran detective with a talent for finding contradictions, following evidence, and distrusting just about everyone.

Marlowe isn't given the answer to a case. He's given access to an investigation environment and has to decide what evidence to examine, connect information across sources, develop theories, and determine what the evidence actually supports.

His personality may be dramatic.

His evidence can't be.

## 🔎 The Idea

LooseThread explores a simple question:

**What happens when an AI agent is placed inside a mystery instead of simply being asked to solve one?**

Rather than providing the entire mystery inside a prompt, cases exist as information Marlowe must actively discover.

The long-term goal is to create an interactive investigation environment where a user acts almost like a game master: creating cases, suspects, evidence, witnesses, hidden truths, and red herrings.

Marlowe becomes one of the players.

## 🕵️ Marlowe

Marlowe has spent twenty years looking at things people would rather keep buried.

He's tired, cynical, suspicious, and probably overdue for a vacation he isn't going to take.

But underneath the personality is an important rule:

**Suspicion is not evidence.**

Marlowe can develop theories and follow hunches, but his conclusions should remain grounded in information he can actually discover.

He should distinguish between:

- What the evidence establishes
- What the evidence suggests
- What he suspects
- What remains unexplained

Sometimes the most important part of an investigation is the thing that doesn't fit.

## 📁 v0.1.0 — Evidence Locker

The first version of LooseThread introduces Marlowe's **Evidence Locker**.

Cases are stored within an isolated filesystem that Marlowe can autonomously investigate using tools.

Marlowe can currently:

- Discover available directories
- Navigate case directories
- Discover files
- Read supported textual evidence
- Connect information across multiple files
- Identify contradictions
- Develop evidence-based theories
- Recognize gaps in the available evidence
- Suggest additional investigative steps

Filesystem access is restricted to Marlowe's designated investigation workspace.

### Example

A case might contain:

```text
cases/
└── 002/
    ├── crime_report.txt
    ├── suspects.txt
    ├── security.log
    ├── employee_records.txt
    └── scene_evidence.txt
```

The user doesn't need to tell Marlowe which files matter.

They can simply tell him:

```text
Marlowe, Case 002 just landed on your desk.
See what you can make of it.
```

Marlowe must determine how to investigate the case himself.

For example, one file might establish that badge `A113` belongs to Bradley while another records `A113` entering the building during the crime window.

Neither file contains the conclusion.

Marlowe has to make the connection.

## 🧵 Loose Threads

Finding a likely explanation doesn't necessarily mean the investigation is finished.

Marlowe is encouraged to identify evidence that doesn't fit his current theory.

A case might strongly implicate a suspect while still leaving questions such as:

- Who actually possessed a badge when it was used?
- Why was a boot print found near a window locked from the inside?
- Whose fingerprints are on the suspected tool?
- Is an apparent clue evidence or coincidence?

These unresolved questions are the **loose threads**.

Future versions of LooseThread will make them an increasingly important part of how Marlowe investigates.

## 🏗️ Current Architecture

```text
User
 │
 ▼
Marlowe
 │
 ├── list directories
 ├── list files
 └── read files
 │
 ▼
Evidence Locker
 │
 ▼
Reason over discovered evidence
 │
 ▼
Investigation Report
```

LooseThread currently uses:

- Python
- LangChain
- LangGraph
- OpenAI models
- `pathlib`
- `puremagic`

## 🚧 Where LooseThread Is Going

The Evidence Locker is only the first environment Marlowe will eventually be able to investigate.

Planned ideas include:

**Case Board**  
Structured facts, suspects, theories, contradictions, open leads, and unresolved loose threads.

**The Street**  
Controlled access to external websites where clues may be hidden across pages, source code, APIs, or other public information.

**Department Records**  
Structured databases and APIs containing employee records, vehicles, incidents, identities, and other investigative information.

**Communications Archive**  
Emails, messages, call records, and other communications that Marlowe can search when relevant.

**Forensics Lab**  
Specialized tools for analyzing evidence rather than simply retrieving it.

**Witness Interviews**  
Independent witness agents with private knowledge, personalities, incomplete perspectives, and limited opportunities for questioning.

The eventual goal is for the user to build an entire case while keeping the underlying truth hidden from Marlowe.

Then the investigation begins.

## 🎲 The Long-Term Vision

LooseThread is part detective agent, part mystery game, and part agent experimentation environment.

Imagine creating:

```text
THE TRUTH
        ↓
Locations ─ Evidence ─ Records
     │         │          │
 Suspects   Red Herrings  Timeline
     │         │          │
     └──── Witnesses ─────┘
                ↓
             Marlowe
                ↓
          Investigation
                ↓
             Theory
```

The person creating the case knows what actually happened.

Marlowe doesn't.

His job is to find out.

## 📌 Project Status

**Current version:** `v0.1.0 — Evidence Locker`

LooseThread is an experimental project under active development.

Right now, the goal isn't to make Marlowe omniscient.

It's to see how good an investigator he can become when he has to earn his answers.
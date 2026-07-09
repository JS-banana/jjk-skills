# Demand Radar

Demand Radar is the demand-mining context for finding evidence-backed user pain
points and preparing validated records for a Feishu Base.

## Language

**Demand Signal**:
A concrete, evidence-backed user or workflow pain that can be reduced to a
scene, job, obstacle, current workaround, and productable opportunity.
_Avoid_: Idea, trend, product list

**Candidate**:
A raw lead collected from search, social posts, comments, reviews, complaints,
services, procurement, or forums before it passes the evidence gate.
_Avoid_: Record, row

**Original Evidence**:
The source text, review, comment, listing, complaint, or procurement detail read
from the concrete URL before judging a candidate.
_Avoid_: Search result, summary, snippet

**Secondary Signal**:
A comment, reply, review, rating, order count, budget, or cross-source mention
that strengthens or weakens a candidate after the original evidence is read.
_Avoid_: Engagement

**Job Sentence**:
The concise JTBD form that says when the user is stuck, what progress they want,
why it matters, and what workaround they use now.
_Avoid_: Feature description, solution pitch

**Evidence Gate**:
The hard acceptance filter that separates demand signals from bugs, feature
requests, trends, recommendations, ads, and vague ideas.
_Avoid_: Scoring rubric

**Acquisition Mode**:
The chosen way to find candidates before keyword choice, such as community feed,
review mining, comment mining, paid workflow, procurement, alternatives, or
search probe.
_Avoid_: Query list

**Native Lexicon**:
Platform-specific phrases observed in the source language and community,
maintained through hit/miss notes rather than direct translation.
_Avoid_: Translated keywords

**Search Probe**:
A targeted query used to improve recall after the source plan is clear.
_Avoid_: Primary evidence

**Parked Candidate**:
A real-looking demand missing exactly one gate, saved for the next deep run to
complete instead of being rejected.
_Avoid_: Soft reject, backlog

**Feishu Row**:
The final validated shape written to the demand Base after a candidate passes
the evidence gate and is mapped to the current schema.
_Avoid_: Note, report

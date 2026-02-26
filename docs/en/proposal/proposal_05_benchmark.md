# Proposal 05: Exploring Dynamic Evaluation for Continual Learning Based on Long-Horizon Human Interaction

## Research Background and Core Motivation

Current evaluations in Continual Learning predominantly rely on static benchmark datasets. However, as the capabilities of Large Language Models (LLMs) advance, static datasets may have inherent limitations in reflecting a model's true long-term memory retention and long-horizon reasoning ability (e.g., the risk of overfitting due to data contamination).

To more realistically assess model performance in complex, long-horizon continual learning scenarios, **this proposal plans to explore a dynamic evaluation scheme based on real human feedback.** The idea is to leverage human users' sensitivity to "whether the model has maintained consistency with historically established settings" as a useful complement to traditional automated evaluation metrics.

### Experimental Sandbox: Structured State-Machine-Based Text Interaction Environment

To conduct this research, one possible entry point is to repurpose the structured interaction sandbox environment from my personal side project, the Anify engine. Alternatively, other open-source options (e.g., text adventure / TRPG engines) could also be considered for an initial pilot.

Taking Anify as an example, such an environment encompasses not only free-form natural language interaction but also maintains a structured state machine at the underlying level, including but not limited to:

- **Character relationship graph**: e.g., numerical affinity values and summaries of key interaction history.
- **Environment and task state**: e.g., triggered event flags and task completion progress.

**Preliminary rationale for adopting this environment:**
This interaction mode combining "natural language + structured state" may provide a good observation point for continual learning. Over extended time spans, model-generated text must remain logically consistent with the underlying structured state. For instance, the model should not forget prior key plot points or alter already-established character relationships. My intuition is that user feedback correcting "memory contradictions" in this setting could be a high-quality data signal, but this still requires validation.

## Exploratory Hypotheses

### H1 (Complementary Value of Human Feedback)

In long-horizon narrative or interactive scenarios, user feedback based on real interactions may expose consistency breakdowns in the model's knowledge retention more effectively than current static automated metrics.

### H2 (State Machine as Anchor)

The underlying structured state set (e.g., attribute values, event records) can serve as an objective probe for automatically detecting whether model-generated text exhibits implicit knowledge drift or factual conflicts.

## Preliminary Experimental Design

The initial idea is to attempt collecting the following evaluation dimensions in a controlled, small-scale environment:

### 1. Preliminary A/B Side-by-Side Evaluation

At critical dialogue turns involving long-horizon memory recall (e.g., triggering historically significant events), two base models (or memory retention strategies) generate outputs in parallel in the background. Test users can be invited to indicate preferences based on "narrative coherence" and "degree of no-forgetting," thereby observing strategy differences over long text spans.

### 2. Interactive Consistency Correction Feedback

A lightweight correction mechanism is introduced in the user interface (e.g., "setting deviation" or "memory error" labels). The goal is to collect and analyze the subjective Error Correction Rate across continuous multi-turn dialogues under different architectures, exploring its feasibility as a forgetting penalty metric.

### 3. Objective Consistency Detection via State Probes

In addition to subjective feedback, periodic detection scripts can be deployed in the background to compare the implicit representations in the model's recent dialogue against anchoring points in the physical state set. This allows observation of the objective rate at which the model's output tendency drifts from established baselines after long-sequence input, without targeted training.

## Resource Requirements and Preliminary Assessment

As an application-oriented evaluation exploration, the compute requirements are relatively low. The main challenges lie in engineering environment setup and early-stage test data acquisition:

- **Engineering**: Initial effort is needed to build the communication pipeline and data collection instrumentation for the sandbox platform.
- **Compute**: For a preliminary pilot (e.g., with dozens of controlled test participants), inference costs can be covered by existing lab API quotas or local deployment of small-to-medium-scale open-source models.
- **Implementation plan**: It is recommended to first run the full data loop in an extremely simplified micro-scenario (e.g., single NPC interaction), validate the method's feasibility, and then consider enriching the scenario dimensions.

## Expected Discussion Value

1. **Broadening the evaluation perspective**: Attempt to introduce a dynamic use-case-based evaluation approach to the continual learning field, and discuss the role of real human-in-the-loop data in mitigating over-reliance on static benchmarks.
2. **Accumulating empirical data**: By collecting interaction data containing real forgetting pain points and human corrections, this may provide early data samples for subsequent long-horizon alignment research on large models (e.g., RLHF / DPO).
3. **Exposing real pain points**: Intuitively establish a realistic baseline and optimization target for subsequent in-depth research on long-term memory mechanisms.

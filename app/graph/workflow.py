from langgraph.graph import StateGraph
from langgraph.graph import END

from app.graph.state import AgentState

from app.agents.ocr.agent import (
    ocr_agent
)

from app.agents.extraction.agent import (
    extraction_agent
)

from app.agents.retrieval.agent import (
    retrieval_agent
)

from app.agents.coding.agent import (
    coding_agent
)

from app.agents.audit.agent import (
    audit_agent
)

from app.agents.qa.agent import (
    qa_agent
)

from app.agents.supervisor.agent import (
    supervisor_agent
)

workflow = StateGraph(
    AgentState
)

workflow.add_node(
    "ocr",
    ocr_agent
)

workflow.add_node(
    "extraction",
    extraction_agent
)

workflow.add_node(
    "retrieval",
    retrieval_agent
)

workflow.add_node(
    "coding",
    coding_agent
)

workflow.add_node(
    "audit",
    audit_agent
)

workflow.add_node(
    "qa",
    qa_agent
)

workflow.add_node(
    "supervisor",
    supervisor_agent
)

workflow.set_entry_point(
    "ocr"
)

workflow.add_edge(
    "ocr",
    "extraction"
)

workflow.add_edge(
    "extraction",
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "coding"
)

workflow.add_edge(
    "coding",
    "audit"
)

workflow.add_edge(
    "audit",
    "qa"
)

workflow.add_edge(
    "qa",
    "supervisor"
)

workflow.add_edge(
    "supervisor",
    END
)

graph = workflow.compile()
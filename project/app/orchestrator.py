from app.agents.tenant_agent import evaluate_tenant_risk
from app.mcp.contracts.evaluate_tenant_contract import EvaluateTenantOutput

def dubi_evaluate_tenant(req):
    tenant_result = evaluate_tenant_risk(req)

    if tenant_result["score"] >= 70:
        status = "APPROVED"
    elif tenant_result["score"] >= 40:
        status = "REVIEW"
    else:
        status = "REJECTED"

    return EvaluateTenantOutput(
        status=status,
        score=tenant_result["score"],
        reason=", ".join(tenant_result["reasons"])
    )
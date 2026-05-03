This is a comprehensive, well-structured research brief with a clear, existing draft in `Variables-Metrics.md`. I now have strong grounding from both the file and external research. I'll produce the full structured report.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

---

# Apex AI — Deep Research Report: Interchange, Handoff, Workflow & Variable Simplification

---

## 1. Executive Summary

The Apex Orientation Core v0 variable model (Value / Time Pressure / Leverage / Fit + confidence + policy lane + hard flags) is **architecturally sound, well-grounded in established practice, and should become the v1 standard**. The four core scores map cleanly onto WSJF's Cost of Delay components (Business Value + Time Criticality + Risk Reduction/Opportunity Enablement / Job Size), with Fit serving as a practical proxy for job-size inversion. The handoff, session trace, and state artifact system needs clearer separation between _trace artifacts_ (immutable, append-only) and _state artifacts_ (delta-updated, canonical) — a distinction directly supported by event-sourcing and CQRS architecture patterns. Pattern learning must remain in a candidate-only pipeline until explicit operator promotion occurs.geeksforgeeks+1[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

---

## 2. Recommended Apex Variable Model

The proposed four-score model is validated by five prioritization frameworks compared below.

## Prioritization Framework Comparison

|Framework|Core Variables|Scoring|Matches Apex Core|Key Limitation|
|---|---|---|---|---|
|**WSJF (SAFe)**|Business Value + Time Criticality + Risk Reduction / Job Size|Ratio formula|✅ Strong — Value, Time Pressure, Leverage all map to Cost of Delay components|Job Size must be estimated [agility-at-scale](https://agility-at-scale.com/safe/lpm/wsjf-weighted-shortest-job-first/)|
|**RICE**|Reach × Impact × Confidence / Effort|Composite score|🟡 Partial — Confidence appears; Reach has no direct Apex analog|Requires user data; heavy for personal planning [routine](https://routine.co/blog/posts/rice-ice-moscow-saasy)|
|**ICE**|Impact × Confidence × Ease|Multiplication|🟡 Partial — Ease ≈ Fit; drops Reach; faster than RICE|Lacks time-pressure signal explicitly [goalsandprogress](https://goalsandprogress.com/moscow-vs-rice-vs-ice-comparison/)|
|**MoSCoW**|Must / Should / Could / Won't|Categorical|🟡 Maps to P0–P3 classes but offers no granularity within class|Political; not derivable from data [goalsandprogress](https://goalsandprogress.com/moscow-vs-rice-vs-ice-comparison/)|
|**Eisenhower Matrix**|Urgent × Important|2×2 quadrant|🟡 Urgent ≈ Time Pressure; Important ≈ Value; lacks Leverage and Fit|Only 2 variables — underfits complex project work|

**Verdict:** Apex's 4-variable model is a practical synthesis of WSJF's Cost of Delay (Value + Time Pressure + Leverage) with a Fit axis not present in WSJF but critical for personal execution planning. It avoids RICE's data-heaviness and Eisenhower's oversimplification.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

## Variable Roles

- **Value (0–3):** Absorbs `strategic_value`. Answers "why does this matter?" Must be derivable from project brief without new research.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Time Pressure (0–3):** Absorbs `deadline_pressure` and `risk_if_deferred`. Risk if deferred **must not** be a separate field — it is the defining property of time pressure itself.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Leverage (0–3):** Absorbs `dependency_unlock`. Answers "what does this unblock or compound?" This is WSJF's "Risk Reduction/Opportunity Enablement" component.[agility-at-scale](https://agility-at-scale.com/safe/lpm/wsjf-weighted-shortest-job-first/)

- **Fit (0–3):** Absorbs `readiness_of_inputs` + `calendar_fit` + `operator_constraint_fit`. Effort should **not** be a separate score — high effort degrades fit, making them functionally identical at the planning level.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)


## Control Fields

- **Confidence:** Must be a _display-only epistemic modifier_, not part of the score. A P1 item with `confidence: low` should be visually flagged but not downgraded — it needs operator attention, not algorithmic demotion.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Policy Lane:** Must be a _guardrail_, not a score variable. It encodes standing allocation rules (Leela / Master of Arts / Wildcard) that exist independent of task value.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Hard Flags:** Must **short-circuit scoring entirely**. A `blocked` task cannot receive a craft flow regardless of its V/T/L/F scores. Flags must be evaluated before the priority class is assigned.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)


## Priority Class Rules

text

`apex_priority_class_v1:   P0:  # must_handle_now — evaluated before craft-flow assignment    triggers:      - hard_deadline AND time_pressure == 3      - hygiene_hold      - operator_decision_needed == true AND blocks_downstream == true      - calendar_conflict AND no_alternate_window  P1:  # should_receive_craft_flow_today    rule: (value >= 2 AND fit >= 2) OR (time_pressure == 3 AND fit >= 1) OR (leverage == 3 AND fit >= 2)    notes: At most 4 P1 items per day; excess must defer.  P2:  # valid_default_lane_work    rule: policy_lane is set AND fit >= 2 AND no hard_flags  P3:  # defer_or_backlog    rule: fit <= 1 OR blocked OR missing_input OR no_actionable_next_step`

---

## 3. Artifact Taxonomy

## Artifact Ownership and Lifecycle

|Artifact|Owner|Consumer(s)|Type|Mutability|
|---|---|---|---|---|
|Session Export|Operator (Alfred scaffolds)|Night, MetaOps, KB Ops|Trace|**Immutable after submission**|
|Night Plan|Night process|Alfred, MetaOps|Synthesis|Immutable once delivered|
|Project Packet|Night / MetaOps / OpState|Alfred|Planning input|Replaced per cycle|
|Daily Command Board|Alfred|Operator, MetaOps|Planning surface|Operator-editable until locked|
|Craft Flow Handoff|Alfred|MetaOps|Execution request|Immutable once sent|
|MetaOps Workflow Package|MetaOps|Operator, Alfred|Execution plan|Versioned, not edited in-place|
|OpState Delta Candidate|Alfred / Session Export|OpState|State proposal|Applied only after operator approval|
|Tracking Record|Alfred (from Board + Export)|Pattern Library, Rhythm|Learning signal|Append-only|
|Pattern Candidate|Alfred / Night|KB Ops|Learning candidate|**Not canonical** — requires promotion|

## Mandatory / Optional Field Rules

For **every** artifact, the following fields are **mandatory**:

- `artifact_id`, `artifact_type`, `project_id`, `created_by`, `created_at`, `source_artifacts[]`


The following are **prohibited in all artifacts**:

- Full session chat logs (these are traces, not structured artifacts)

- Mood, energy, or subjective state fields (excluded explicitly in v1)[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- Unreviewed pattern candidates presented as canonical facts


---

## 4. Handoff Best Practices and Apex Checklist

## Established Handoff Models

Five established handoff protocols are directly applicable to Apex:

1. **SBAR (Situation–Background–Assessment–Recommendation):** From medicine and aviation. Proven to reduce communication failures — studies show 80%+ improvement in handoff satisfaction when SBAR is standardized. Maps to Apex as: Situation = current state, Background = source artifacts, Assessment = orientation scores, Recommendation = requested action.[academia](https://www.academia.edu/65847619/Implementation_of_the_SBAR_Checklist_to_Improve_Patient_Safety_in_the_United_States_Air_Force_Aeromedical_Evacuation)

2. **IPASS (Illness severity–Patient summary–Action list–Situational awareness–Synthesis):** Pediatric transport handoff. The "synthesis" and "situational awareness" steps directly justify Apex's `stop_condition` and `decision_needed` fields.[academia](https://www.academia.edu/65847619/Implementation_of_the_SBAR_Checklist_to_Improve_Patient_Safety_in_the_United_States_Air_Force_Aeromedical_Evacuation)

3. **NATO SALUTE:** Military intelligence handoff (Size, Activity, Location, Unit, Time, Equipment). Establishes that handoffs must include _bounded context_, not full history.

4. **Incident Command System (ICS) Briefing:** Operational period handoff in emergency response. Requires: current status, assigned objectives, resource constraints, known unknowns, and explicit successor identification. Supports Apex's `return_to: Alfred` field.

5. **Agile Sprint Review → Planning handoff:** Velocity actuals, accepted vs. rejected outputs, carry-forward items, next sprint objectives. Directly maps onto the Session Export → Night Plan cycle.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)


## What Causes Handoff Failure

- Missing stop condition (consumer doesn't know when to stop and return)[academia](https://www.academia.edu/65847619/Implementation_of_the_SBAR_Checklist_to_Improve_Patient_Safety_in_the_United_States_Air_Force_Aeromedical_Evacuation)

- Ambiguous authority (who has decision rights is unclear)

- Trace artifact mistaken for state artifact — "the chat log says X" replacing "OpState says X"

- Over-specified input that forces rework before work begins

- Missing constraint declaration (`must_avoid`, `must_use`) causing MetaOps to produce unusable output[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)


## Apex Handoff Validation Checklist

Every handoff from Alfred to MetaOps **must** pass:

text

`apex_handoff_validation_v1:   identity:    - [ ] handoff_id assigned    - [ ] source_artifacts listed (minimum: project_packet_id)    - [ ] target_consumer named  intent:    - [ ] objective is a single, bounded statement    - [ ] expected_outputs are enumerable (not "good work")    - [ ] stop_condition is explicit  constraints:    - [ ] time_container_min is set    - [ ] must_use and must_avoid declared (even if empty [])  routing:    - [ ] return_to is named    - [ ] operator_decision_needed is boolean, not blank  state_effect:    - [ ] opstate_delta_candidate is boolean    - [ ] pattern_candidate is boolean`

---

## 5. Session Trace vs. Live State

## The Core Distinction

Event sourcing distinguishes between the **event log** (immutable sequence of what happened) and the **current state** (projection rebuilt from events). Apex must enforce the same separation:[geeksforgeeks](https://www.geeksforgeeks.org/system-design/difference-between-cqrs-and-event-sourcing/)

- **Session Export = event log entry.** It is a bounded trace of what happened in one craft flow. It must never be edited retroactively. CQRS terminology: the write-side record.[geeksforgeeks](https://www.geeksforgeeks.org/system-design/difference-between-cqrs-and-event-sourcing/)

- **OpState = current state projection.** It contains only the latest known truth per project. It must be updated via **delta candidates**, not by replacing itself with session text.


## OpState Delta Candidate Rules

A delta candidate **must** specify:

- `field_path`: which OpState field is being proposed for change

- `old_value`: what the field currently says

- `proposed_value`: what it should say after this session

- `evidence`: session_export_id that supports the change

- `operator_approved`: false (default) — applied only when operator signs off


Full session traces must **never** enter OpState. Doing so converts a trace into a false source of truth and causes downstream drift.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

## Session Export Scaffold — Minimizing Operator Burden

The prefilled scaffold (generated by Night, reviewed by Alfred) should reduce operator input to three categories only:

|Field category|Format|Owner|
|---|---|---|
|Actuals vs. planned|Checkbox deviation flags|Operator (5–10 checkboxes)|
|Deviation reason|≤ 2 sentences free text|Operator (only if checkbox is checked)|
|Next highest-impact tasks|Ordered list, max 3|Operator|
|Everything else|Pre-filled by Alfred / Night|AI — operator corrects only|

The `learning` section (pattern candidates, chunk candidates) should be **inferred by Alfred from the deviation flags**, not operator-written. The operator may promote or reject candidates, but must not be required to author them.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

---

## 6. Recommended Artifact Schemas

## Project Packet v1 (recommended)

text

`project_packet_v1:   identity:                       # MANDATORY    packet_id:                    # PP-{date}-{project}-{seq}    project_id:    source_artifacts: []          # night_plan_id, session_export_id, opstate_ref  proposed_work:                  # MANDATORY    task:                         # Single bounded statement    expected_outputs: []          # Enumerable, max 4    next_action:                  # First physical action  orientation:                    # MANDATORY    value: 0-3    time_pressure: 0-3    leverage: 0-3    fit: 0-3    confidence: low|medium|high    policy_lane: leela|master_of_arts|wildcard|none    hard_flags: []    priority_class: P0|P1|P2|P3  routing:                        # MANDATORY    recommended_flow: CF1|CF2|CF3|CF4    requested_metaops_action:    operator_decision_needed: false  state_effect:                   # MANDATORY — all boolean    opstate_delta_candidate: true|false    pattern_candidate: true|false    kb_candidate: true|false  # PROHIBITED: full session logs, mood, energy, speculative value estimates`

## Daily Command Board v1 (recommended changes from v0)

The v0 board is slightly over-specified at the craft-flow level. Recommended changes:

- **Remove** `physical_chunk`, `mental_chunk`, `break_or_regen_chunk` from craft-flow entries — move to a separate `rhythm_profile` block to avoid conflating work planning with regeneration scheduling.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Add** `operator_locked: true|false` to each craft-flow — once the operator confirms, the board must not auto-mutate.

- **Keep** `risks_and_repairs` — this is the board's explicit P0 surface. Do not merge it with the priority stack.

- **Cognitive load target:** The board must be comprehensible in under 90 seconds. Research on dashboard design recommends 5–9 information chunks maximum (Miller's Law); four craft flows + one risk section + one deferred list equals 6 chunks — within bounds.


text

`daily_command_board_v1:   identity:    date:    generated_at:    source_window:                # night_plan_id(s) used    operator_locked: false  calendar_reality:    hard_locks: []    available_work_windows: []  daily_priority_stack: []        # Ranked project_packet references with priority_class  craft_flows:    - flow_id: CF1|CF2|CF3|CF4      lane: leela_1|leela_2|master_of_arts|wildcard      time_window:      project_id:      objective:      expected_outputs: []      craft_template:      metaops_handoff_needed: true|false      operator_decision_needed: false      operator_locked: false  rhythm_profile:                 # Separated from craft flows    physical_chunk:    mental_chunk:    break_or_regen_chunk:    afterwork_plan:  deferred_or_not_today: []  risks_and_repairs: []           # P0 items only`

## MetaOps Craft Flow Handoff v1

The v0 is close to correct but `requested_metaops_outputs` is too prescriptive — MetaOps should decide its own output format for a given sprint template. Recommended reduction:

text

`metaops_craft_flow_handoff_v1:   identity:                       # MANDATORY    handoff_id:    flow_id:    project_id:    source_artifacts: []  intent:                         # MANDATORY    target_output:                # Single bounded deliverable    expected_outputs: []          # Max 4, enumerable    priority_reason:              # ≤ 2 sentences from orientation    stop_condition:               # When MetaOps is done    return_to: Alfred  constraints:                    # MANDATORY    time_container_min: 120    sprint_template:    must_use: []    must_avoid: []    operator_decision_needed: false  requested_outputs:              # SIMPLIFIED — MetaOps chooses format    - sprint_workflow             # MANDATORY    - acceptance_criteria         # MANDATORY    - session_export_expectation  # MANDATORY    - prompt_chain                # OPTIONAL    - ai_routing_plan             # OPTIONAL  # PROHIBITED: full project background, KB content, personal planning context`

## Session Export v1

text

`session_export_v1:   metadata:                       # MANDATORY — auto-filled by scaffold    session_id:    project_id:    flow_id:    session_date:    scaffold_source: night_plan_id  actuals:                        # OPERATOR-ENTERED — checkboxes + short text    objective_met: true|false|partial    outputs_delivered: []         # List only delivered items    deviations: []                # Checked boxes; reason if checked    blockers_found: []    next_highest_impact_tasks: [] # Max 3, ordered  candidates:                     # INFERRED BY ALFRED — operator approves/rejects    opstate_delta_candidates: []    pattern_candidates: []    kb_candidates: []  downstream:                     # AUTO-FLAGGED by Alfred    metaops_processing_needed: true|false    night_plan_input: true|false    promotion_review_needed: true|false  # PROHIBITED: full chat transcripts, speculative strategy, mood/energy`

## Tracking Record v1 — Evaluation

The v1 schema from the brief is minimum viable and correct. Key automation opportunities:[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

|Field|Automatable?|Rule|
|---|---|---|
|`planned.*`|✅ Yes|Copy from Daily Command Board at lock time|
|`actual.flow_completion`|🟡 Partial|Alfred infers from Session Export `objective_met`|
|`actual.outputs`|🟡 Partial|Alfred copies from `outputs_delivered`|
|`process_learning.*`|❌ No|Operator must enter — this is the core signal|
|`candidates.*`|✅ Yes|Alfred generates; operator approves|

Fields to **remove** from Tracking Record: `bp_xp` (not authoritative), `mood`, `energy` — correctly excluded in v1 already.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

---

## 7. Pattern Learning and Candidate Promotion

## Established Practice: Candidate-to-Canonical Pipeline

Knowledge management systems distinguish between _tacit knowledge capture_ (observation), _codification_ (candidate form), and _validation_ (canonical promotion). The Apex Pattern Library correctly implements this three-stage model.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

## Detection Threshold

A pattern candidate should be **detected** when:

- The same workflow or prompt chain succeeds in ≥ 2 independent sessions for the same project type, OR

- A deviation from expected outputs has the same root cause across ≥ 2 sessions


A candidate should be **promoted** to canonical only when:

- Operator explicitly approves it in KB Ops review

- It has been used successfully ≥ 3 times across ≥ 2 different projects or time periods

- It is not contradicted by any operator correction in the record


## Rejection and Archival

Rejected candidates **must** be archived, not deleted. Archive format should preserve: candidate_id, detection_date, rejection_date, rejection_reason (operator free text), source_tracking_records. This prevents the same candidate from re-surfacing without new evidence.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

## Anti-Overfitting Rule

**Must not** promote a pattern based on fewer than 3 occurrences. **Must not** promote a pattern learned exclusively from the first 10 sessions of a new workflow (insufficient baseline). Night and Alfred should flag candidates that appear in early sessions with `confidence: low` until a baseline is established.

---

## 8. Daily / Weekly / Monthly Planning

## Daily Command Board Design

Research on human factors in dashboards supports a maximum of **7 ± 2 information chunks** (Miller's Law) for a command surface. The Apex board at 4 craft flows + 1 risk section + 1 deferred section + 1 calendar reality = **7 chunks** — correct.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- Afterwork regeneration (`rhythm_profile`) must be **visually separated** from craft-flow sessions. Mixing them causes the operator to unconsciously treat regen as productive output — a known burnout precursor in personal productivity research.

- Hard calendar locks must be **declared before craft-flow assignment** — not filled in around already-assigned flows. This mirrors ICS operational planning doctrine (constraints first, then resource allocation).


## Weekly Rollup

Weekly rhythm planning should aggregate from Tracking Records, not from Session Exports directly. The rollup needs only:

- Planned vs. actual craft-flow completion rate (%)

- Per-project velocity (sessions delivered vs. planned)

- Recurring blockers (same blocker appearing ≥ 2 days)

- Pattern candidate count (total pending KB Ops review)


Monthly planning should be **directional only** — no craft-flow assignments, no task decomposition. It should contain: 3–5 directional objectives per project lane, known hard dates, and a weekly capacity estimate. Over-scheduling months is a well-documented failure mode in OKR implementations where quarterly goals crowd each other out.

---

## 9. What to Remove or Simplify

|Element|Recommendation|Reason|
|---|---|---|
|`deadline_pressure` as separate field|✅ Remove — fold into `time_pressure`|Redundant [Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)|
|`risk_if_deferred` as separate field|✅ Remove — it _defines_ time pressure|Tautological [Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)|
|`default_lane_alignment` as score|✅ Remove — it is `policy_lane`|Not a value variable [Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)|
|`operator_constraint_fit` as separate field|✅ Remove — fold into `fit`|Absorbed [Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)|
|`physical_chunk` / `mental_chunk` in craft-flow entries|✅ Move to `rhythm_profile`|Category error — planning vs. execution|
|`requested_metaops_outputs` as prescriptive list|🟡 Simplify to mandatory/optional|MetaOps must choose format|
|Full `learning` section in Session Export authored by operator|✅ Shift to Alfred inference|Reduces burden without losing signal|
|`mood` / `energy` / `bp_xp`|✅ Excluded — maintain exclusion|Not authoritative in v1 [Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)|
|Scoring formula (weighted sum)|✅ Do not implement — use classification rules|Formula creates false precision and will be ignored|

---

## 10. Risks and Anti-Patterns

- **Session Export becoming SSOT:** The highest risk. Prevent by making OpState the only canonical project truth surface, with explicit delta-candidate gating.[geeksforgeeks](https://www.geeksforgeeks.org/system-design/difference-between-cqrs-and-event-sourcing/)[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Night mutating OpState silently:** Night must produce _proposals_ only. Every OpState change requires an `operator_approved: true` flag before application.[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

- **Over-scoring small tasks:** Applying full V/T/L/F scoring to trivial hygiene tasks creates compliance fatigue. P0 `hygiene_hold` tasks should bypass orientation scoring entirely.

- **Pattern library becoming shadow doctrine:** If Alfred surfaces pattern candidates in handoffs before KB Ops promotion, consumers will treat them as canonical. Candidates must be visually distinguished (e.g., `[CANDIDATE]` prefix) in all artifacts.

- **Craft-flow overflow:** Assigning 5+ P1 items when only 4 craft flows exist. Alfred must enforce a hard cap of 4 assigned flows per day; excess P1 items go to `deferred_or_not_today` with an explicit reason.

- **MetaOps receiving underspecified handoffs:** A handoff without `stop_condition` forces MetaOps to self-terminate, producing variable-length output that Alfred cannot reliably process.[academia](https://www.academia.edu/65847619/Implementation_of_the_SBAR_Checklist_to_Improve_Patient_Safety_in_the_United_States_Air_Force_Aeromedical_Evacuation)


---

## 11. Implementation Roadmap

## v0 — Skeleton (establish the spine)

- Implement `apex_orientation_core_v0` schema (V/T/L/F + confidence + policy_lane + hard_flags)

- Implement Project Packet v1 schema

- Implement Daily Command Board v1 schema (no rhythm profile yet)

- Implement Craft Flow Handoff v1 schema

- Alfred manually applies priority class rules; no automation

- Session Export uses scaffold but operator fills all fields manually


## v1 — Automation layer

- Night generates pre-filled Session Export scaffolds

- Alfred auto-fills `planned.*` in Tracking Record from locked board

- Alfred infers `opstate_delta_candidate` list from Session Export deviations

- OpState delta candidates require explicit operator approval before application

- Pattern candidate detection active (≥ 2 session threshold)


## v1.1 — Learning integration

- KB Ops review workflow active — candidates surface for operator promotion/rejection

- Weekly rollup auto-generated from Tracking Records

- Alfred surfaces `confidence: low` flags on early-session patterns

- Rhythm profile added to Daily Command Board


## Later (v2 / Leela productization)

- Pattern library feeds Leela app workflows (not Alfred runtime)

- Monthly Direction Map auto-seeded from KB-promoted patterns

- Multi-project dependency tracking across OpState surfaces

- Automated WSJF-style scoring calibration from Tracking Record actuals


---

## 12. Open Questions Requiring Operator Decision

1. **Effort field:** Should effort be explicit (e.g., `effort: 0-3`) or remain implicit in `fit`? Explicit effort enables WSJF-style ratio scoring in the future but adds a fifth scoring axis now.[agility-at-scale](https://agility-at-scale.com/safe/lpm/wsjf-weighted-shortest-job-first/)[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)

2. **P0 override authority:** Can Alfred auto-assign a P0 task to CF1 without operator review, or must every P0 surface for confirmation first?

3. **Confidence threshold for MetaOps handoff:** Should Alfred block a handoff if `confidence: low` and `fit <= 1`, or surface it with a warning?

4. **Pattern promotion quorum:** Is operator-alone sufficient for KB promotion, or should it require 3 successful uses + operator approval?

5. **Weekly Rhythm Plan:** Should it be generated by Alfred from Tracking Records automatically, or remain a manual operator-authored artifact with Alfred input?


---

## Source Bibliography

- WSJF formula and SAFe prioritization:scrum-master+2

- RICE vs. ICE vs. MoSCoW comparison:goalsandprogress+1

- SBAR handoff protocol and aviation/medicine evidence:corescholar.libraries.wright+1

- CQRS and Event Sourcing — trace vs. state distinction:youngju+1

- Multi-agent AI orchestration patterns (LangGraph, CrewAI):linkedin+1

- Apex AI Variables-Metrics design document:[Variables-Metrics.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/9d02ba1c-39cc-4ad2-b001-cf3442ad5651/Variables-Metrics.md?AWSAccessKeyId=ASIA2F3EMEYE4ZQXY26J&Signature=FAZJz42ZJRDxgQm5%2B48S2WNMKMM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJIMEYCIQD7qDVFnl%2Fj0%2FiPY8MW8yuBq%2BVFzw81%2BoUid%2FEyJ%2BkpvQIhANokRXovjSUHibS4Y6cbF1quIfZOkg6b5q%2BEe21Yhf7vKvMECCYQARoMNjk5NzUzMzA5NzA1IgwxLsi360%2FwhDj2GNcq0ASc8eRcyACOCK2m%2BHLChTgBWRhp5uLes5M3%2BpcvfBSBjBJwNa47F6i3%2FuBx3X%2FvpSRmXII6Pxhv2Hy45%2B9blQzYAfUzivlKrIanxk70ie40yN%2BnaWulb9qU036pr75MceaA17Yu%2FPwANSrS18PMMbw9Qbye3uvnM08QRDE84nL9egqpSZEQhu9Hdg1n966oRsutu%2FDpx270iIW8ipBkcYJNpVzLXIzsuKSL1sd28FoY9hMj5EJQJoo6dqrmSGcWWAHoDo9%2BXZbwtI8YS%2BxZ5GKu7BK08E1Fxu9cnTbYf%2FGpwLLKaexOm6p8BPPUvE4nZC1ecWhML76wb%2BhrEU66BcGDgGY7CwlBSgHZJS9BiDdKGpIQK4sKlNr9OjxHmWmuM2LzMN9y36gnl1B%2BY3RI%2FKqwSId3wcoPIF%2F6WIczBhasyeW50y3nR%2BqhgePlWiWgnpFdUZd760QzJvgatuuEfSVPDKKIb1q5prvaf0%2FuP6QpMlSL7LcWPCb%2BfVRRo1MMZKfaPT1R%2Bs9qq9I%2Bt3k4P2a%2F4b7bRDelbf%2FEcxDdWHilKNFzCgD8Ci6RmM4AOq%2FcRKpL5wIpF0u8A6UBNB88%2Fr9C8TPvUgLftR%2BXH2pbvY2xzg3I%2FKqdyw79IdWeLxSiNg0w1ypJpZDDlZMQ7x8p48v0ra%2FTv40dkywurelj8WY7uUpK8n1UwOtg3%2BVb%2FB9gkjKHcGzPzdCxUAVtJqb28NSEEaCwReJe7An7mAMGXx7Rpy2e2t3Yyv2jHEJsY5T9P%2BRrwiT0KsWfql1RZlnYbjCoML2%2B0s8GOpcBHsJQGbr5wyn7sq%2BXgIK6ZUSS4i5HMuuSt9g1rQVplU7XzEgzPJ3mQR8XHhrmrHBENh1uFTvCqruf8eEyZ6LUQ%2B8Dt3xyF14rA9%2BLS7mNsXo%2F%2B7SIEn2PllmbGgYWjhg0PzwOTz47tTfdeKvmF%2FGlncYsJ3DIUmFVpCRUMJgx2EnHWFAS4jxygxcSX1t8hADDeFjhTH9o5Q%3D%3D&Expires=1777640630)
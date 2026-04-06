# HW2 Report
# HW2 Report

## Business Use Case

The system is designed as a customer support assistant that helps generate responses to customer inquiries. This can be useful for companies that receive a high volume of customer messages and want to provide fast, consistent, and professional replies.

---

## Model Choice

I used the Google Gemini (gemini-2.0-flash) model for this project. The model was chosen because it is fast, cost-efficient, and performs well for text generation tasks such as customer support responses.

During testing, the model successfully generated polite and professional replies. However, API quota limits occasionally caused a "429 RESOURCE_EXHAUSTED" error, which is unrelated to the system design.

---

## Baseline vs. Final Design

The initial prompt was simple and only instructed the model to respond politely. As a result, the responses were basic and sometimes lacked structure or empathy.

After revising the prompt multiple times, I added instructions to:
- maintain a professional tone
- avoid making unrealistic promises (e.g., refunds)
- acknowledge customer emotions
- ask for additional information when needed

These improvements led to responses that were more consistent, empathetic, and aligned with real customer support practices.

---

## Limitations and Failure Cases

The system still has several limitations. The responses can be generic and lack specific details because the model does not have access to real customer data or company policies.

Additionally, the system cannot verify order status or take real actions, so human review is still required for sensitive cases such as refunds or complaints.

---

## Deployment Recommendation

I would recommend deploying this system as a support tool rather than a fully automated solution. It can assist human agents by drafting responses, but human oversight should be required before sending messages to customers.

With additional context, such as access to order data or internal systems, the performance of the system could be further improved.
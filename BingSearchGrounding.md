what data are being sent as queries?
use public web data for grounding?

Short answer: Microsoft says the service uses **public web data for grounding**, but your prompts/search queries sent to Grounding with Bing Search are **not automatically made public on the web**. However, the queries and related metadata **are sent to Bing services outside the normal Azure compliance boundary**, and are governed by Bing’s own terms and processing policies. ([Microsoft Learn][1])

Key distinctions from the docs:

* Grounding with Bing Search “uses Bing to search over public web data” — meaning the *source content* comes from publicly indexed websites. ([Microsoft Learn][1])
* Microsoft explicitly states:

  > “only the Bing search query, tool parameters, and your resource key are sent to Bing” ([Microsoft Learn][1])
* It also states:

  > “your customer data is transferred outside of the Azure compliance boundary to the Grounding with Bing Search service” ([Microsoft Learn][1])

So the practical interpretation is:

| Question                                                                                    | Answer                                                                          |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Is my query sent to Bing?                                                                   | Yes                                                                             |
| Is it processed outside Azure AI Foundry compliance boundary?                               | Yes                                                                             |
| Is it used to search public web content?                                                    | Yes                                                                             |
| Is my query itself published publicly on the internet?                                      | No indication of that                                                           |
| Can Microsoft log/store it for service operation, billing, abuse prevention, quality, etc.? | Likely yes under Bing/Microsoft service terms                                   |
| Should sensitive/confidential data be sent?                                                 | Microsoft strongly implies you should assess compliance/privacy needs carefully |

The most important privacy/compliance sentence is this one:

> “Grounding with Bing Search is not subject to the same data processing terms … and does not have the same compliance standards and certifications as the Foundry Agent Service.” ([Microsoft Learn][1])

That is essentially Microsoft warning enterprise users:

* don’t assume the same Azure OpenAI data isolation guarantees,
* and don’t send sensitive regulated data unless your compliance team approves it.

What the docs do **not** explicitly say:

* that your prompts are used to train public Bing models,
* that prompts become publicly searchable,
* or that other customers can see them.

So:

* **Not public** in the sense of “visible on Bing search.”
* But **not fully isolated/private in the same Azure-compliance sense either**. Queries are processed by Bing systems under separate terms.

[1]: https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/bing-grounding?utm_source=chatgpt.com "How to use Grounding with Bing Search in Foundry Agent Service (classic) - Microsoft Foundry (classic) portal | Microsoft Learn"


grounding with bing search azure ai foundry
[https://www.microsoft.com/en-us/bing/apis/grounding-legal]
[https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/bing-grounding ]


Introducing GPT-5.5
GPT-5.5 is now available in Codex. It's our strongest agentic coding model yet, built to reason through large codebases, check assumptions with tools, and keep going until the work is done. It uses more quota per token than GPT-5.4, but needs fewer tokens to get the job done. Learn more



Warning
Grounding with Bing Search is a First Party Consumption Service  governed by the Grounding with Bing terms of use and the Microsoft Privacy Statement.

The Microsoft Data Protection Addendum does not apply to data sent to Grounding with Bing Search. When Customer uses Grounding with Bing Search, Customer Data will flow outside the Azure compliance and Geo boundary. This also means use of Grounding with Bing Search waives all elevated Government Community Cloud security and compliance commitments, to include data sovereignty and screened/citizenship-based support, as applicable.

Use of Grounding with Bing Search will incur costs; learn more about pricing.

Learn more about how Azure admins can manage access to use of Grounding with Bing Search.



The normal enterprise/privacy contractual protections Microsoft offers for many Azure and Microsoft cloud services do NOT apply to Grounding with Bing Search.


grounding with bing search azure ai foundry
https://www.microsoft.com/en-us/bing/apis/grounding-legal
https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/bing-grounding 


Introducing GPT-5.5
GPT-5.5 is now available in Codex. It's our strongest agentic coding model yet, built to reason through large codebases, check assumptions with tools, and keep going until the work is done. It uses more quota per token than GPT-5.4, but needs fewer tokens to get the job done. Learn more

https://learn.microsoft.com/en-us/azure/foundry/agents/overview?WT.mc_id=Portal-Microsoft_Bing_Api

Warning
Grounding with Bing Search is a First Party Consumption Service  governed by the Grounding with Bing terms of use and the Microsoft Privacy Statement.

The Microsoft Data Protection Addendum does not apply to data sent to Grounding with Bing Search. When Customer uses Grounding with Bing Search, Customer Data will flow outside the Azure compliance and Geo boundary. This also means use of Grounding with Bing Search waives all elevated Government Community Cloud security and compliance commitments, to include data sovereignty and screened/citizenship-based support, as applicable.

Use of Grounding with Bing Search will incur costs; learn more about pricing.

Learn more about how Azure admins can manage access to use of Grounding with Bing Search.



The normal enterprise/privacy contractual protections Microsoft offers for many Azure and Microsoft cloud services do NOT apply to Grounding with Bing Search.



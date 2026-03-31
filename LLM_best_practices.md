Best practices for LLM prompt engineering

Writing effective prompts - a process known as prompt engineering - is essential for unlocking the full potential of large language models. The goal of prompt engineering is to design inputs that guide LLMs to generate desired outputs. The quality of a prompt directly influences the relevance, accuracy, and coherence of the model's responses. This guide provides some best practices for prompt engineering, along with illustrative examples. While the effectiveness of each strategy might vary depending on the LLM used, the following is a consideration of best practices helping you start engineering useful and accurate prompts.

If you are working with AIP Assist specifically, review our AIP Assist best practices.
Key strategies for effective prompting

Effective prompt engineering is a dynamic and iterative process that combines clarity, specificity, and contextual relevance. By following these best practices and incorporating examples, users can maximize the effectiveness of large language models. As AI technology evolves, staying informed about new strategies will further enhance prompt quality and output accuracy.

    Be clear and specific
        Be clear: Use straightforward language to define the task or question.
            Example: Instead of asking "What do you know about coding?", specify "Summarize my framework options for developing a web application."
        Specify context: Provide context to anchor the model's response.
            Example: "As a software engineer, explain the benefits of abstraction."

    Refine and iterate
        Test and adjust: Experiment with different prompt structures and refine them based on output quality.
            Example: Start with "List the advantages of web applications." If the response is too broad, refine to "List the maintenance benefits of web applications compared to native applications."
        Feedback loop: Use model feedback to continuously improve prompt design.
            Example: If the model misunderstands a prompt, adjust the wording and re-test.

    Use examples
        Demonstrate desired output: Provide examples to set expectations for format and content.
            Example: "Translate the following sentence to French: 'Hello, how are you?' Example: 'Hello' translates to 'Bonjour'."
        Highlight patterns: Use examples to establish a consistent response pattern.
            Example: "For each fruit, list its color and taste. Example: Apple - Red, Sweet."

    Manage length and complexity
        Be concise: Provide necessary details without overloading the model.
            Example: Instead of "Can you tell me about the history, current state, and future of robotics?", use "Briefly describe the history of robotics."
        Avoid overloading: Break complex tasks into simpler parts.
            Example: "First, list the steps in the semiconductor manufacturing process. Then, explain each step in detail."

    Incorporate constraints
        Set boundaries: Define clear constraints to guide response scope.
            Example: "Summarize the article in no more than three sentences."
        Limit unwanted outputs: Use negative examples or explicit instructions.
            Example: "Generate a list of pros and cons of remote work, but exclude personal opinions."

    Provide relevant context
        Align with model capabilities: Tailor prompts to the strengths and limitations of the model.
            Example: For a model trained on medical data, ask, "Explain the symptoms of diabetes," rather than unrelated topics.
        Maintain relevance: Ensure prompts are relevant to the model's training data.
            Example: "Discuss recent advancements in AI," aligning with the model's knowledge base.

    Optimize the interaction
        Role-playing: Assign roles to guide the model's tone and depth.
            Example: "As a mechanical engineer, describe the most important sensors to deploy in a heavy manufacturing process."
        Sequential prompting: Use a series of prompts for complex responses.
            Example: "First, describe the semiconductor manufacturing process. Next, list three types of semiconductors and how they are manufactured."

# Prompt engineering overview

---

## Before prompt engineering

This guide assumes that you have:
1. A clear definition of the success criteria for your use case
2. Some ways to empirically test against those criteria
3. A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out [Define success criteria and build evaluations](/docs/en/test-and-evaluate/develop-tests) for tips and guidance.

<CardGroup cols={2}>
  <Card title="Prompt generator" icon="link" href="/dashboard">
    Don't have a first draft prompt? Try the prompt generator in the Claude Console!
  </Card>
  <Card title="Prompting best practices" icon="link" href="/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">
    For model-specific tuning guidance for Claude's latest models, start here.
  </Card>
</CardGroup>

***

## When to prompt engineer

  This guide focuses on success criteria that are controllable through prompt engineering.
  Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

***

## How to prompt engineer

All prompting techniques — from clarity and examples to XML structuring, role prompting, thinking, and prompt chaining — are covered in [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). That's the living reference; start there.

The [Claude Console](/dashboard) also offers [prompting tools](/docs/en/build-with-claude/prompt-engineering/prompting-tools)—prompt generator, templates and variables, and prompt improver—to help you build and refine prompts quickly.

***

## Prompt engineering tutorial

If you're an interactive learner, you can dive into our interactive tutorials instead!

<CardGroup cols={2}>
  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>
  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>

Prompt engineering techniques

These techniques aren't recommended for reasoning models like gpt-5 and o-series models.

Prompt construction can be difficult. In practice, the prompt acts to help the model complete the desired task, but it's more of an art than a science, often requiring experience and intuition to craft a successful prompt. The goal of this article is to help get you started with this learning process. This article attempts to capture general concepts and patterns that apply to all GPT models. However, it's important to understand that each model behaves differently, so the learnings might not apply equally to all models.

Note

For current API guidance and examples, see Responses API and Azure OpenAI in Microsoft Foundry Models API reference.
Basics

This section covers the basic concepts and elements of GPT prompts.

Text prompts are how users interact with GPT models. As with all generative language models, GPT models attempt to produce the next series of words that are most likely to follow from the previous text. It's as if we're saying What is the first thing that comes to your mind when I say <prompt>? The examples below demonstrate this behavior. Given the first words of famous content, the model is able to accurately continue the text.
Prompt 	Completion
Four score and seven years ago our 	fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. […]
"Call me Ishmael." 	"Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world." […]

As you develop more complex prompts, it's helpful to keep this fundamental behavior in mind. Regardless of the prompt that is provided, the model is simply responding with what it determines is most likely (given its training data and training targets). If you ask a question in your prompt, the model isn't following a separate “Q&A” code path, but rather it appears to answer the question because an answer is the most likely sort of response for the given question as input.
Prompt components

When using the Completion API while there's no differentiation between different parts of the prompt, it can still be useful for learning and discussion to identify underlying prompt components. With the Chat Completion API there are distinct sections of the prompt that are sent to the API in the form of an array of dictionaries with associated roles: system, user, and assistant. This guidance focuses more generally on how to think about prompt construction rather than providing prescriptive guidance that is specific to one API over another.

It's also important to understand that while there could be other valid ways to dissect prompts, the goal of this breakdown is to provide a relatively simple way to think about prompt construction. With the Completion API, all the components are optional, but at least one must be present and most prompts include more than one component. There can be some grey area between components as well. The order presented below roughly corresponds to how commonly each component is used, from most to least.
Instructions

Instructions are likely the most commonly used prompt component. Instructions are simply that: instructions to the model on what to do. While simple in concept, they can be complex in practice. The following table illustrates this by showing both simple and more complex instructions, in two different forms.
Instruction Type 	Prompt 	Completion
Simple instructions 	Write an introduction for a weekly newsletter. 	Welcome to our weekly newsletter. This week we have a special focus on productivity. We'll be sharing tips and tricks on how to be productive in all areas of your life. We hope you enjoy and please share with your friends!
Complex instructions 	Write an introduction for a weekly newsletter to my company named Contoso. It should mention the great all hands meeting we had last week and thank the team for all their hard work over the tough past few months. 	Welcome to Contoso's weekly newsletter! We had a great all hands meeting last week and I want to thank the team for all their hard work over the tough past few months. We're looking forward to a bright future and I'm confident that with our team's dedication and commitment, we'll achieve great things. Thank you for being a part of our team and I look forward to working with you all in the coming weeks and months. Sincerely, [Your name].
Complex Instructions 	Write an introduction for a weekly newsletter, including the following:
- My company is named contoso
- An exuberant greeting
- Thanking the team for their hard work over a couple tough months
- Positive outlook for the coming quarter
- Signed by the SLT 	Hello Contoso team! I wanted to take a moment to thank you for all your hard work over the past few months. It's been a tough couple of months, but you've all pulled together and done an amazing job. I'm really proud of you all. Looking ahead to the next quarter, I'm feeling really positive. I think we're going to achieve some great things. Thanks again, The Senior Leadership Team.
Primary Content

Primary content refers to some sort of text that is being processed or transformed by the model. Primary content is typically used in conjunction with instructions. A simple example would be language translation. In the example below, the English text would be considered the primary content while "Translate to French:" is an instruction.
Prompt 	Completion
Can you please tell me how to get to the museum?
Translate to French: 	Pouvez-vous s'il vous plaît me dire comment aller au musée?

Primary content can also be much longer. In the following example, the primary content is the introduction section from the Wikipedia entry on time complexity, which is almost 300 words long. This content is abbreviated in our table for ease of display.
Prompt 	Completion
In computer science, the time complexity is the computational complexity that describes the amount of computer time it takes to run an algorithm. Time complexity is commonly estimated by [...]
Summarize the previous text in a few sentences: 	Time complexity is a measure of how long an algorithm takes to run. It's typically expressed as a function of the size of the input. The most common measure is worst-case time complexity, which is the maximum amount of time required for inputs of a given size.
In computer science, the time complexity is the computational complexity that describes the amount of computer time it takes to run an algorithm. Time complexity is commonly estimated by [...]
TL;DR (Too long didn't read) 	The time complexity of an algorithm is the amount of time it takes to run an algorithm. Time complexity is commonly estimated by counting the number of elementary operations performed by the algorithm, supposing that each elementary operation takes a fixed amount of time to perform. The time complexity is generally expressed as a function of the size of the input.

GPT models can also handle primary content that is structured. In the example below, a TSV about beers in Belgium (abbreviated for display in this article) is passed to the model as part of the prompt. It's capable of properly interpreting the content and answering questions about the data.
Prompt 	Completion
Belgian Beer Brands
Beer name Beer style color ABV Brewery
"Chimay Gold: ""Doree""" trappist pale ale gold 4.80% Chimay Brewery (official trappist)
"Chimay Blue: ""Grande Reserve""" trappist dark ale dark 9.00%
[…]
Referencing the table above, how many beers are less than 6% ABV? 	There are 10 beers in the table that are less than 6% ABV.
Examples

Successful prompts often rely on the practice of “one-shot” or “few-shot” learning. This refers to the inclusion of one or more examples of the desired behavior of the model, typically by including input and output pairs. This isn't learning in the sense that the model is permanently changed, but rather that the examples better condition the model to respond as desired for only the current inference. The use of prompts with no examples is sometimes referred to as “zero-shot” learning. Note that with the Chat Completion API few-shot learning examples are typically added to the messages array in the form of example user/assistant interactions after the initial system message.
Learning Type 	Prompt 	Completion
Zero-shot 	Headline: Coach confident injury won't derail Warriors
Topic: 	The coach is confident that the injury won't derail the Warriors' season. The team is still focused on their goals and that they'll continue to work hard to achieve them.
Few-shot 	Headline: Twins' Correa to use opt-out, test free agency
Topic: Baseball
Headline: Qatar World Cup to have zones for sobering up
Topic: Soccer
Headline: Yates: Fantasy football intel for Week 6
Topic: Football
Headline: Coach confident injury won't derail Warriors
Topic: 	Basketball

The example above illustrates the utility of few-shot learning. Without the examples, the model seems to be guessing at the desired behavior, while the examples cleanly show the model how to operate. This also demonstrates the power of the model, it can infer the category of label that is wanted, even without a "basketball" label in the examples.
Cue

Cues act as the "jumpstart" for the output of the model, helping to direct the model to the desired output. It's often a prefix that the model can build onto. In the example below, we show the cue directing the story to include key elements. Cues are often used along with instructions, but not always. In the examples below, the model is being used to summarize a long announcement email. A cue is used in one case to help focus the output of the model and to suggest a specific output format (bullet points) in the other.

In the context of the Chat Completion API instructions take the form of the system message, and few-shot examples are indicated by providing a series of example user/assistant interactions to help prime the model.
Number of Cues 	Prompt 	Completion
0 	Performance reviews are a core component of our Performance & Development approach at Contoso. […]
Summarize the above email message: 	The purpose of this email is to inform employees of recent changes to the performance review experience, which is part of Contoso's Performance & Development approach. The changes include an improved structure, upgraded in-tool user experience, and focused prompts. Additionally, there's now an optional Conversation Starters section for employees to flag topics they'd like to discuss with their managers.
1 	Performance reviews are a core component of our Performance & Development approach at Contoso. […]
Summarize the above email message:
The key takeaway of the message is 	that Contoso is improving the performance review experience by making it more focused on core priorities, expectations, and impact. Additionally, they're upgrading the in-tool user experience with tips, resources, and guidance. Finally, they're adding guidance on how to activate company-wide core priorities.
2 	Performance reviews are a core component of our Performance & Development approach at Contoso. […]
Summarize the above email message:
Key Points:
• 	Contoso is introducing changes to the performance review experience, based on feedback from employees.
• The changes include a new focus on core priorities, expectations, and impact; an upgraded user experience; and new guidance on company-wide core priorities.
• Performance reviews are a time to reflect on past performance and learning as well as to plan for future priorities and growth opportunities.
• Employees and managers should write comments in advance of the performance review meeting.
• There should be at least two performance reviews per year.
• The time investment for each review should remain about the same.
Supporting content

Supporting content is information that the model can utilize to influence the output in some way. It differs from primary content in that it isn't the main target of task, but it's typically used along with primary content. Common examples include contextual information such as the current date, the name of the user, user preferences, and so on. The example below uses supporting content to help organize a set of planned workshops for the user. Without the supporting (important topics) the model simply lists off the workshops (truncated for display), when informed of my important topics, the model is able to accurately group the meetings.
Supporting Content 	Prompt 	Completion
Without 	Workshop list:
Title Description
Planning Workshop Kickoff Please join us to kick off our workshop! Hear from our leaders about cross group priorities and learnings for the year ahead. The invitation to this event has already been sent to everyone in […]
Summarize the workshops above, grouped by topic: 	Workshop list:
Planning Workshop Kickoff
-Planning Workshop Wrap-up
- Core MeetUp
- Customer Driven Perspectives
-Impact and Key Focus Areas
-Best practices
-Accelerating app adoption […]
With 	Workshop list:
Title Description
Planning Workshop Kickoff Please join us to kick off our workshop! Hear from our leaders about cross group priorities and learnings for the year ahead. The invitation to this event has already been sent to everyone in […]
My Important Topics: prompt engineering, search, GPT models
Summarize the workshops above, grouped by my important topics: 	1. Prompt Engineering:
- New prompt engineering tips
- The art of prompt engineering
2. Search:
-Intro to vector search with embedding
3. GPT Models:
- Intro to GPT-4
- GPT-35-Turbo in-depth.
Scenario-specific guidance

The techniques in this section will teach you strategies for increasing the accuracy and grounding of responses you generate with a Large Language Model (LLM). It is, however, important to remember that even when using prompt engineering effectively you still need to validate the responses the models generate. Just because a carefully crafted prompt worked well for a particular scenario doesn't necessarily mean it will generalize more broadly to certain use cases. Understanding the limitations of LLMs, is just as important as understanding how to leverage their strengths.

This guide doesn't go in-depth into the mechanics behind the message structure for Chat Completions. If you aren't familiar with interacting with Chat Completions models programmatically, we recommend reading our how-to guide on the Chat Completion API first.

Note

All of the examples in this section of the guide were tested against a base GPT-4 model in English. Some techniques may produce different results with newer models like gpt-4.1, and gpt-4.5. If you're reading a localized version of this article in another language, these responses represent a localized translation of the English results. To learn more about potential limitations depending on what language you're using to prompt a model, consult our Responsible AI transparency note.
Few-shot learning

A common way to adapt language models to new tasks is to use few-shot learning. In few-shot learning, a set of training examples is provided as part of the prompt to give additional context to the model.

When using the Chat Completions API, a series of messages between the User and Assistant (written in the new prompt format), can serve as examples for few-shot learning. These examples can be used to prime the model to respond in a certain way, emulate particular behaviors, and seed answers to common questions.
System message 	Few-shot examples
Assistant is an intelligent chatbot designed to help users answer their tax related questions.
Instructions
- Only answer questions related to taxes.
- If you're unsure of an answer, you can say "I don't know" or "I'm not sure" and recommend users go to the IRS website for more information. 	User - "When do I need to file my taxes by?"
Assistant - "In 2023, you'll need to file your taxes by April 18th. The date falls after the usual April 15th deadline because April 15th falls on a Saturday in 2023. For more information, see https://www.irs.gov/filing/individuals/when-to-file "

User - "How can I check the status of my tax refund?"
Assistant - "You can check the status of your tax refund by visiting https://www.irs.gov/refunds "

The table above describes the basic prompt structure, but for a detailed explanation of the exact prompt format you'll need to refer to the Chat Completion guide.
Non chat scenarios

While the Chat Completion API is optimized to work with multi-turn conversations, it also can be used for non chat scenarios. For example, for a sentiment analysis scenario, you might use the following prompt:
System message 	User 	Assistant
You're an assistant designed to analyze sentiment from speech data. Users will paste in a string of text and you'll respond with an assessment of the response of the speaker. Rate on a scale of 1-10 (10 being highest). Explain why this rating was given. 	hi thank you for calling contoso pharmacy who am i speaking with today i understand your frustration mary um can you tell me what exactly you're trying to accomplish OK uh certainly happy to check that for you one moment please i see here that you were on a generic form of lipitor is that right OK uh so i see that your doctor stopped prescribing these drugs in twenty twenty one actually OK uh yeah i'd be happy to check that for you uh because sometimes there's a gap in the system and it just doesn't get reported so let me take a look here just a moment so i'm seeing here that your doctor had these drugs prescribed to you from twenty twelve through twenty twenty one OK um yeah according to the latest records uh provided by doctor's office you're now on a different drug metformin would you like us to go ahead and fill that prescription for you for pick up a bit of form in five hundred milligrams uh you're very welcome mary please let us know if there's anything else we can do for you today. 	Sentiment rating: 8
The speaker in this text seems to be polite, helpful, and patient while addressing the concerns of the customer. They take the time to check the information, provide clear explanations, and offer assistance. However, the rating isn't a 10 because there's still a hint of uncertainty in some parts of the conversation, which might not convey complete confidence to the customer.
Start with clear instructions

The sequence information appears in the prompt matters. This is because GPT style models are built in a certain way that defines how they process the input. Our research suggests that telling the model the task you want it to do at the beginning of the prompt, before sharing additional contextual information or examples, can help produce higher-quality outputs.

Note

Although following this technique is still generally recommended, in contrast to previous model versions (GPT-3 and prior), our testing showed that the model response with ChatGPT and GPT-4 models was the same regardless of whether the technique is utilized. In this example, we see that adding the statement “Several sources … eruption” at the beginning or the end of the prompt didn't cause any change in the final model response.
System message 	User 	Assistant
You're an AI assistant that helps people find information. 	Your task is to verify if the statement "Several sources mention a chance of another large eruption" is supported by a specific quote from the following set of snippets.
---
SNIPPETS
[1] 14 percent chance of megaquake hitting Seattle, experts say
SEATTLE - There's a 14 percent chance of a magnitude 9 Cascadia earthquake hitting Seattle in the next 50 years, the U.S. Geological Survey estimates. "Unfortunately, we're unable to...

[2] Earthquake experts lay out latest outlook for Seattle's 'Really Big One’
“We say that there's approximately a 14% chance of another approximately magnitude-9 earthquake occurring in the next 50 years,” said a geophysicist at the University of Washington...
---
Is the statement "Several sources mention a chance of another large eruption" directly implied or stated by the snippets? 	No, the statement isn't directly implied or stated by the snippets. The snippets mention a chance of a "megaquake" and a "magnitude 9 Cascadia earthquake" hitting Seattle in the next 50 years, but don't mention a chance of another large eruption.
Repeat instructions at the end

Models can be susceptible to recency bias, which in this context means that information at the end of the prompt might have more significant influence over the output than information at the beginning of the prompt. Therefore, it's worth experimenting with repeating the instructions at the end of the prompt and evaluating the impact on the generated response.
Prime the output

This refers to including a few words or phrases at the end of the prompt to obtain a model response that follows the desired form. For example, using a cue such as “Here’s a bulleted list of key points:\n- ” can help make sure the output is formatted as a list of bullet points.
System message 	User 	Assistant
You're an AI assistant that helps people find information. Answer in as few words as possible. 	John Smith is married to Lucy Smith. They have five kids, and he works as a software engineer at Microsoft. What search queries should I do to fact-check this? ## One possible search query is: 	"John Smith married Lucy Smith five kids software engineer Microsoft"

In the above prompt, the text One possible search query is: primes the model to produce a single output. Without this cue the model produces several search queries as output.
Add clear syntax

Use clear syntax for your prompt to communicate intent and make outputs easier to parse.

In the example below, separators (--- in this case) have been added between different sources of information or steps. This allows the use of --- as a stopping condition for generation. In addition, section headings or special variables are presented in uppercase to differentiate them.
System message 	User 	Assistant
You're an AI assistant that helps people find information. 	You'll read a paragraph, and then issue queries to a search engine in order to fact-check it. Also explain the queries.
---
PARAGRAPH
John Smith is married to Lucy Smith. They have five kids, and he works as a software engineer at Microsoft. What search queries should I do to fact-check this?
---
QUERIES 	1. "John Smith Microsoft" - To check if John Smith is indeed employed at Microsoft.
2. "John Smith Lucy Smith" - To check if John Smith is married to Lucy Smith.
3. "John Smith children" - To check if John Smith has five children.

If you're not sure what syntax to use, consider using Markdown or XML. The models have been trained on a large quantity web content in XML and Markdown, which might provide better results.
Break the task down

Large language models (LLMs) often perform better if the task is broken down into smaller steps. For example, in the search query prompt referenced earlier, the prompt can be restructured so that the model is first instructed to extract relevant facts, and then instructed to generate search queries that can be used to verify those facts.
System message 	User 	Assistant
You're an AI assistant that helps people find information. 	You'll read a paragraph, and then issue queries to a search engine in order to fact-check it.
---
PARAGRAPH
John Smith is married to Lucy Smith. They have five kids, and he works as a software engineer at Microsoft. What search queries should I do to fact-check this?
---
Now you'll extract factual claims, and issue queries to fact-check them. When issuing a query, use the function SEARCH("query")

FACTUAL CLAIMS 	1. John Smith is married to Lucy Smith
2. They have five kids
3. He works as a software engineer at Microsoft

QUERIES
SEARCH("John Smith married Lucy Smith")
SEARCH("John Smith family size")
SEARCH("John Smith Microsoft software engineer")

Notice the use of clear syntax to differentiate the sections and prime the output. In this simple example, breaking the task down from one to two steps isn't very dramatic, but when trying to do this for a larger piece of text with many factual claims, breaking the task down can make a significant difference.
Use of affordances

Sometimes we can get the model to use an affordance instead of relying on its own parameters for information and answers. Search, for example, can be an affordance to help mitigate against fabricated answers, and to get up-to-date information.

One simple way to use an affordance is to stop generation once the affordance calls are generated by the model, then paste the outcomes back into the prompt. Below is an example of what the follow-up call could be after doing the SEARCH calls above. Notice how we pasted the search results into the prompt and replaced the previous SEARCH calls.
System message 	User 	Assistant
You're an AI assistant that helps people find information. 	You'll read a paragraph, extract factual claims, and then use search engine results to fact-check them
---
PARAGRAPH
John Smith is married to Lucy Smith. They have five kids, and he works as a software engineer at Microsoft. What search queries should I do to fact-check this?
---
FACTUAL CLAIMS
- John Smith is married to Lucy Smith
- John and Lucy have five kids
- John works as a software engineer at Microsoft
---
Here are various search queries issued to research the claims above:
SEARCH QUERIES
- John Smith married to Lucy Smith
- John Smith number of children
- John Smith software engineer Microsoft
---
Here are snippets of the search results:
SNIPPETS:
[1] … John Smith’s wedding was on September 25, 2012 …
[2] … John Smith was accompanied by his wife Lucy to a party
[3]John was accompanied to the soccer game by his two daughters and three sons
[4] … After spending 10 years at Microsoft, Smith founded his own startup, Tailspin Toys
[5] John M is the town smith, and he married Fiona. They have a daughter named Lucy
---
Given the snippets, fact check each of the factual claims above: 	- John Smith is married to Lucy Smith: Confirmed. Snippet [1] and [2] both mention John Smith's wife as Lucy.

- John and Lucy have five kids: Confirmed. Snippet [3] mentions that John was accompanied by his two daughters and three sons.

- John works as a software engineer at Microsoft: Partially confirmed. Snippet [4] mentions that John spent 10 years at Microsoft, but it doesn't explicitly state that he currently works there. Further research might be needed to confirm his current employment status.
Chain of thought prompting

Important

This technique is only applicable non-reasoning models. Attempting to extract model reasoning through methods other than the reasoning summary parameter aren't supported, may violate the Acceptable Use Policy, and may result in throttling or suspension when detected.

This is a variation on the break the task down technique. Instead of splitting a task into smaller steps, in this approach, the model response is instructed to proceed step-by-step and present all the steps involved. Doing so reduces the possibility of inaccuracy of outcomes and makes assessing the model response easier.
System message 	User 	Assistant
You're an AI assistant that helps people find information. 	Who was the most decorated (maximum medals) individual athlete in the Olympic games that were held at Sydney? Take a step-by-step approach in your response, cite sources and give reasoning before sharing final answer in the below format: ANSWER is: <name> 	Step 1: Determine the year of the Sydney Olympic games. The Sydney Olympic games were held in the year 2000.

Step 2: Find a list of individual athletes who won multiple medals in the 2000 Sydney Olympics.

According to the official website of the Olympic Games, there were several individual athletes who won multiple medals in the 2000 Sydney Olympics. Some of the notable names include:
• Ian Thorpe (Australia) - 3 gold, 2 silver, 0 bronze
• Pieter van den Hoogenband (Netherlands) - 2 gold, 0 silver, 2 bronze
• Lenny Krayzelburg (USA) - 3 gold, 0 silver, 0 bronze
• Inge de Bruijn (Netherlands) - 3 gold, 1 silver, 0 bronze

Step 3: Determine the athlete with the most medals. After reviewing the list of individual athletes who won multiple medals in the 2000 Sydney Olympics, we can see that the athlete with the most medals is Ian Thorpe from Australia, who won a total of 5 medals (3 gold and 2 silver).

Therefore, the ANSWER is: Ian Thorpe.
Specifying the output structure

Using your prompt to specify the structure of the output can have a significant effect on the nature and quality of the results. Sometimes system message inputs as “only write true facts” or “don't fabricate information” might not be adequate mitigations. Instead, asking for the model response to also include citations can help result in a reduction of the prevalence of incorrect responses.

If you instruct the model to cite the source material when it makes statements, those statements are much more likely to be grounded. Asking for citations makes it so that the model must make two errors every time it generates a response: the first error is the fabricated response, and the second is the bad citation. Note that the closer the citation is to the text it supports, the shorter the distance ahead the model needs to anticipate the citation, which suggests that inline citations are better mitigations for false content generation than citations at the end of the content.

Similarly, if you ask the model to extract factual statements from a paragraph, it might extract compound statements such as ‘X is doing Y AND Z’ (which can be harder to verify). This can be avoided by specifying an output structure such as (entity1, relationship, entity2).

This example shows the use of citations and directing the model response to fit a defined structure.
System message 	User 	Assistant
You're an AI assistant that helps people find information 	List down the different behaviors exhibited by the Customer Support agent in the following conversation.
---
hi thank you for calling contoso pharmacy who am i speaking with today i understand your frustration mary um can you tell me what exactly you're trying to accomplish OK uh certainly happy to check that for you one moment please i see here that you were on a generic form of lipitor is that right OK uh so i see that your doctor stopped prescribing these drugs in twenty twenty one actually OK uh yeah i'd be happy to check that for you uh because sometimes there's a gap in the system and it just doesn't get reported so let me take a look here just a moment so i'm seeing here that your doctor had these drugs prescribed to you from twenty twelve through twenty twenty one OK um yeah according to the latest records uh provided by doctor's office you're now on a different drug metformin would you like us to go ahead and fill that prescription for you for pick up a bit of form in five hundred milligrams uh you're very welcome mary please let us know if there's anything else we can do for you today.
---
How was the response of the Customer Support agent?
Classify and list down their various behaviors and cite the reason behind the classification, using the format BEHAVIOR("reason") 	1. Polite Greeting BEHAVIOR("Agent starts the conversation with a polite greeting and asks for the caller's name")
2. Empathetic BEHAVIOR("Agent acknowledges Mary's frustration and tries to understand her concern")
3. Attentive BEHAVIOR("Agent listens to the customer's problem and asks for more details")
4. Proactive BEHAVIOR("Agent offers to check the issue for the customer")
5. Informative BEHAVIOR("Agent provides the relevant information about the customer's prescription history")
6. Thorough BEHAVIOR("Agent checks for any possible gaps in the system and provides a complete response")
7. Confirmatory BEHAVIOR("Agent confirms the current medication with the customer")
8. Solution-oriented BEHAVIOR("Agent offers to fill the new prescription for the customer")
9. Courteous BEHAVIOR("Agent thanks the customer and offers further assistance if needed")
System message 	User 	Assistant
You're an AI assistant that helps people find information. 	Cluster the following news headlines into topic categories based on patterns seen within the text. Also mention reasoning behind how these categories were defined.
Output format:
{
"TOPIC_NAME": "",
"HEADLINES": [],
"REASONING": ""
}

Input news headlines:
1. "From books to presentations in 10s with AR + ML"
2. "Demo from 1993 of 32-year-old Yann LeCun showing off the World's first Convolutional Network for Text Recognition"
3. "First Order Motion Model applied to animate paintings"
4. "Robinhood and other brokers literally blocking purchase of $GME, $NOK, $BB, $AMC; allow sells"
5. "United Airlines stock down over 5% premarket trading"
Output:
	
{
"ARTIFICIAL_INTELLIGENCE": {
"HEADLINES": [
"From books to presentations in 10s with AR + ML,"
"Demo from 1993 of 32-year-old Yann LeCun showing off the World's first Convolutional Network for Text Recognition,"
"First Order Motion Model applied to animate paintings"
],
"REASONING": "These headlines are related to artificial intelligence, machine learning, and their applications in various fields."
},
"FINANCIAL_MARKETS": {
"HEADLINES": [
"Robinhood and other brokers literally blocking purchase of $GME, $NOK, $BB, $AMC; allow sells,"
"United Airlines stock down over 5% premarket trading",
"Bitcoin was nearly $20,000 a year ago today"
],
"REASONING": "These headlines are related to financial markets, stocks, cryptocurrencies, and trading platforms."
}
}
Temperature and Top_p parameters

Changing the temperature parameter changes the output of the model. The temperature parameter can be set between 0 and 2. A higher value, for example 0.7 makes the output more random and produce more divergent responses, while a lower value, like. 0.2, makes the output more focused and concrete. A fictional story could be generated using a higher temperature. Whereas to generate a legal document it's recommended to use a much lower temperature. Top_probability is another parameter and is similar to Temperature in that it also controls the randomness of the model response, but it does so in a different way. The general recommendation is to alter one of these two parameters at a time, not both.
Provide grounding context

One of the most effective ways to provide reliable answers is to give the model data to draw its responses from (grounding data). If your use case relies on up-to-date, reliable information and isn't purely a creative scenario, we strongly recommend providing grounding data. In general, the closer you can get your source material to the final form of the answer you want, the less work the model needs to do, which means there's less opportunity for error. Here's an example where the system is provided a blog describing the launch of GPT-4 in Azure OpenAI in Microsoft Foundry Models, and asked to name some of its early customers.
System message 	User 	Assistant
You're an AI assistant that helps people find information. You'll provide answers exclusively from below text and respond in 100 words or less:
"At Microsoft, we're constantly discovering new ways to unleash creativity, unlock productivity, and up level skills so that more people can benefit from using AI. This is allowing our customers to …

… thereby reducing the likelihood that the model generates a harmful response.”1

Answer in 100 words or less. Use bullet lists wherever possible. 	Who are some of the early customers of the Azure OpenAI GPT-4 models? 	Here are some of the early customers of the Azure OpenAI GPT-4 models:
- Epic Healthcare: They plan to use GPT-4 to help physicians and nurses spend less time on data entry and investigation.
- Coursera: They're using Azure OpenAI with GPT-4 to create a new AI-powered learning experience on their platform.
- Coca-Cola: They're using Azure OpenAI to build a knowledge hub and plan to leverage GPT-4's multimodal capabilities for marketing, advertising, public relations, and customer relations.
- Other companies of all sizes are using Azure AI to improve customer experiences, summarize long-form content, help write software, and reduce risk by predicting the right tax data.

1 Text from Azure OpenAI GPT-4 launch blog.
Best practices

    Be Specific. Leave as little to interpretation as possible. Restrict the operational space.
    Be Descriptive. Use analogies.
    Double Down. Sometimes you might need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc.
    Order Matters. The order in which you present information to the model might impact the output. Whether you put instructions before your content (“summarize the following…”) or after (“summarize the above…”) can make a difference in output. Even the order of few-shot examples can matter. This is referred to as recency bias.
    Give the model an “out”. It can sometimes be helpful to give the model an alternative path if it's unable to complete the assigned task. For example, when asking a question over a piece of text you might include something like "respond with "not found" if the answer isn't present." This can help the model avoid generating false responses.

Space efficiency

While the input size increases with each new generation of GPT models, there will continue to be scenarios that provide more data than the model can handle. GPT models break words into "tokens." While common multi-syllable words are often a single token, less common words are broken in syllables. Tokens can sometimes be counter-intuitive, as shown by the example below which demonstrates token boundaries for different date formats. In this case, spelling out the entire month is more space efficient than a fully numeric date.

Screenshot of a string of text with highlighted colors delineating token boundaries.

Given this limited space, it's important to use it as efficiently as possible.

    Tables – As shown in the examples in the previous section, GPT models can understand tabular formatted data quite easily. This can be a space efficient way to include data, rather than preceding every field with name (such as with JSON).
    White Space – Consecutive whitespaces are treated as separate tokens, which can be an easy way to waste space. Spaces preceding a word, on the other hand, are typically treated as part of the same token as the word. Carefully watch your usage of whitespace and don’t use punctuation when a space alone will do.

Note: The author created this article with assistance from AI. Learn more

Best practices for prompt engineering with the OpenAI API

How to give clear and effective instructions to OpenAI models
Updated: 3 hónappal ezelőtt
How prompt engineering works

Due to the way OpenAI models are trained, there are specific prompt formats that work particularly well and lead to more useful model outputs.

The official prompt engineering guide by OpenAI is usually the best place to start for prompting tips.

Below we present a number of prompt formats we find work well, but feel free to explore different formats, which may fit your task better.
Rules of Thumb and Examples

Note: the "{text input here}" is a placeholder for actual text/context
1. Use the latest model

For best results, we generally recommend using the latest, most capable models. Newer models tend to be easier to prompt engineer.

Note: There are some differences to consider when prompting a reasoning model versus prompting a GPT model. More details here.
2. Put instructions at the beginning of the prompt and use ### or """ to separate the instruction and context

Less effective ❌:

Summarize the text below as a bullet point list of the most important points.

{text input here}

Better ✅:

Summarize the text below as a bullet point list of the most important points.

Text: """
{text input here}
"""

3. Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc

Be specific about the context, outcome, length, format, style, etc

Less effective ❌:

Write a poem about OpenAI. 

Better ✅:

Write a short inspiring poem about OpenAI, focusing on the recent DALL-E product launch (DALL-E is a text to image ML model) in the style of a {famous poet}

4. Articulate the desired output format through examples

Less effective ❌:

Extract the entities mentioned in the text below. Extract the following 4 entity types: company names, people names, specific topics and themes.

Text: {text}

Show, and tell - the models respond better when shown specific format requirements. This also makes it easier to programmatically parse out multiple outputs reliably.

Better ✅:

Extract the important entities mentioned in the text below. First extract all company names, then extract all people names, then extract specific topics which fit the content and finally extract general overarching themes

Desired format:
Company names: <comma_separated_list_of_company_names>
People names: -||-
Specific topics: -||-
General themes: -||-

Text: {text}

5. Start with zero-shot, then few-shot, neither of them worked, then fine-tune

✅ Zero-shot

Extract keywords from the below text.

Text: {text}

Keywords:

✅ Few-shot - provide a couple of examples

Extract keywords from the corresponding texts below.

Text 1: Stripe provides APIs that web developers can use to integrate payment processing into their websites and mobile applications.
Keywords 1: Stripe, payment processing, APIs, web developers, websites, mobile applications
##
Text 2: OpenAI has trained cutting-edge language models that are very good at understanding and generating text. Our API provides access to these models and can be used to solve virtually any task that involves processing language.
Keywords 2: OpenAI, language models, text processing, API.
##
Text 3: {text}
Keywords 3:

✅Fine-tune: see fine-tune best practices here.
6. Reduce “fluffy” and imprecise descriptions

Less effective ❌:

The description for this product should be fairly short, a few sentences only, and not too much more.

Better ✅:

Use a 3 to 5 sentence paragraph to describe this product.

7. Instead of just saying what not to do, say what to do instead

Less effective ❌:

The following is a conversation between an Agent and a Customer. DO NOT ASK USERNAME OR PASSWORD. DO NOT REPEAT.

Customer: I can’t log in to my account.
Agent:

Better ✅:

The following is a conversation between an Agent and a Customer. The agent will attempt to diagnose the problem and suggest a solution, whilst refraining from asking any questions related to PII. Instead of asking for PII, such as username or password, refer the user to the help article www.samplewebsite.com/help/faq

Customer: I can’t log in to my account.
Agent:

8. Code Generation Specific - Use “leading words” to nudge the model toward a particular pattern

Less effective ❌:

# Write a simple python function that
# 1. Ask me for a number in mile
# 2. It converts miles to kilometers

In this code example below, adding “import” hints to the model that it should start writing in Python. (Similarly “SELECT” is a good hint for the start of a SQL statement.)

Better ✅:

# Write a simple python function that
# 1. Ask me for a number in mile
# 2. It converts miles to kilometers
 
import

9. Use the Generate Anything feature

Developers can use the 'Generate Anything' feature to describe a task or expected natural language output and receive a tailored prompt.

Learn more about using the 'Generate Anything' feature.
Parameters

Generally, we find that model and temperature are the most commonly used parameters to alter the model output.

    model - Higher performance models are generally more expensive and may have higher latency.

    temperature - A measure of how often the model outputs a less likely token. The higher the temperature, the more random (and usually creative) the output. This, however, is not the same as “truthfulness”. For most factual use cases such as data extraction, and truthful Q&A, the temperature of 0 is best.

    max_completion_tokens (maximum length) - Does not control the length of the output, but a hard cutoff limit for token generation. Ideally you won’t hit this limit often, as your model will stop either when it thinks it’s finished, or when it hits a stop sequence you defined.

    stop (stop sequences) - A set of characters (tokens) that, when generated, will cause the text generation to stop.

For other parameter descriptions see the API reference. 

Write

Sign in
·

Top highlight
My LLM coding workflow going into 2026
Addy Osmani
Addy Osmani
22 min read
·
Dec 19, 2025

AI coding assistants became game-changers this year, but harnessing them effectively takes skill and structure. These tools dramatically increased what LLMs can do for real-world coding, and many developers (myself included) embraced them.

At Anthropic, for example, engineers adopted Claude Code so heavily that today ~90% of the code for Claude Code is written by Claude Code itself. Yet, using LLMs for programming is not a push-button magic experience — it’s “difficult and unintuitive” and getting great results requires learning new patterns. Critical thinking remains key. Over a year of projects, I’ve converged on a workflow similar to what many experienced devs are discovering: treat the LLM as a powerful pair programmer that requires clear direction, context and oversight rather than autonomous judgment.

In this article, I’ll share how I plan, code, and collaborate with AI going into 2026, distilling tips and best practices from my experience and the community’s collective learning. It’s a more disciplined “AI-assisted engineering” approach — leveraging AI aggressively while staying proudly accountable for the software produced.
Press enter or click to view image in full size
Start with a clear plan (specs before code)

Don’t just throw wishes at the LLM — begin by defining the problem and planning a solution.

One common mistake is diving straight into code generation with a vague prompt. In my workflow, and in many others’, the first step is brainstorming a detailed specification with the AI, then outlining a step-by-step plan, before writing any actual code. For a new project, I’ll describe the idea and ask the LLM to iteratively ask me questions until we’ve fleshed out requirements and edge cases. By the end, we compile this into a comprehensive spec.md — containing requirements, architecture decisions, data models, and even a testing strategy. This spec forms the foundation for development.

Next, I feed the spec into a reasoning-capable model and prompt it to generate a project plan: break the implementation into logical, bite-sized tasks or milestones. The AI essentially helps me do a mini “design doc” or project plan. I often iterate on this plan — editing and asking the AI to critique or refine it — until it’s coherent and complete. Only then do I proceed to coding. This upfront investment might feel slow, but it pays off enormously. As Les Orchard put it, it’s like doing a “waterfall in 15 minutes” — a rapid structured planning phase that makes the subsequent coding much smoother.

Having a clear spec and plan means when we unleash the codegen, both the human and the LLM know exactly what we’re building and why. In short, planning first forces you and the AI onto the same page and prevents wasted cycles. It’s a step many people are tempted to skip, but experienced LLM developers now treat a robust spec/plan as the cornerstone of the workflow.
Press enter or click to view image in full size
Break work into small, iterative chunks

Scope management is everything — feed the LLM manageable tasks, not the whole codebase at once.

A crucial lesson I’ve learned is to avoid asking the AI for large, monolithic outputs. Instead, we break the project into iterative steps or tickets and tackle them one by one. This mirrors good software engineering practice, but it’s even more important with AI in the loop. LLMs do best when given focused prompts: implement one function, fix one bug, add one feature at a time. For example, after planning, I will prompt the codegen model: “Okay, let’s implement Step 1 from the plan”. We code that, test it, then move to Step 2, and so on. Each chunk is small enough that the AI can handle it within context and you can understand the code it produces.

This approach guards against the model going off the rails. If you ask for too much in one go, it’s likely to get confused or produce a “jumbled mess” that’s hard to untangle. Developers report that when they tried to have an LLM generate huge swaths of an app, they ended up with inconsistency and duplication — “like 10 devs worked on it without talking to each other,” one said. I’ve felt that pain; the fix is to stop, back up, and split the problem into smaller pieces. Each iteration, we carry forward the context of what’s been built and incrementally add to it. This also fits nicely with a test-driven development (TDD) approach — we can write or generate tests for each piece as we go (more on testing soon).

Several coding-agent tools now explicitly support this chunked workflow. For instance, I often generate a structured “prompt plan” file that contains a sequence of prompts for each task, so that tools like Cursor can execute them one by one. The key point is to avoid huge leaps. By iterating in small loops, we greatly reduce the chance of catastrophic errors and we can course-correct quickly. LLMs excel at quick, contained tasks — use that to your advantage.
Provide extensive context and guidance

LLMs are only as good as the context you provide — show them the relevant code, docs, and constraints.

When working on a codebase, I make sure to feed the AI all the information it needs to perform well. That includes the code it should modify or refer to, the project’s technical constraints, and any known pitfalls or preferred approaches. Modern tools help with this: for example, Anthropic’s Claude can import an entire GitHub repo into its context in “Projects” mode, and IDE assistants like Cursor or Copilot auto-include open files in the prompt. But I often go further — I will either use an MCP like Context7 or manually copy important pieces of the codebase or API docs into the conversation if I suspect the model doesn’t have them.

Expert LLM users emphasize this “context packing” step. For example, doing a “brain dump” of everything the model should know before coding, including: high-level goals and invariants, examples of good solutions, and warnings about approaches to avoid. If I’m asking an AI to implement a tricky solution, I might tell it which naive solutions are too slow, or provide a reference implementation from elsewhere. If I’m using a niche library or a brand-new API, I’ll paste in the official docs or README so the AI isn’t flying blind. All of this upfront context dramatically improves the quality of its output, because the model isn’t guessing — it has the facts and constraints in front of it.

There are now utilities to automate context packaging. I’ve experimented with tools like gitingest or repo2txt, which essentially “dump” the relevant parts of your codebase into a text file for the LLM to read. These can be a lifesaver when dealing with a large project — you generate an output.txt bundle of key source files and let the model ingest that. The principle is: don’t make the AI operate on partial information. If a bug fix requires understanding four different modules, show it those four modules. Yes, we must watch token limits, but current frontier models have pretty huge context windows (tens of thousands of tokens). Use them wisely. I often selectively include just the portions of code relevant to the task at hand, and explicitly tell the AI what not to focus on if something is out of scope (to save tokens).

I think Claude Skills have potential because they turn what used to be fragile repeated prompting into something durable and reusable by packaging instructions, scripts, and domain specific expertise into modular capabilities that tools can automatically apply when a request matches the Skill. This means you get more reliable and context aware results than a generic prompt ever could and you move away from one off interactions toward workflows that encode repeatable procedures and team knowledge for tasks in a consistent way. A number of community-curated Skills collections exist, but one of my favorite examples is the frontend-design skill which can “end” the purple design aesthetic prevalent in LLM generated UIs. Until more tools support Skills officially, workarounds exist.

Finally, guide the AI with comments and rules inside the prompt. I might precede a code snippet with: “Here is the current implementation of X. We need to extend it to do Y, but be careful not to break Z.” These little hints go a long way. LLMs are literalists — they’ll follow instructions, so give them detailed, contextual instructions. By proactively providing context and guidance, we minimize hallucinations and off-base suggestions and get code that fits our project’s needs.
Press enter or click to view image in full size
Choose the right model (and use multiple when needed)

Not all coding LLMs are equal — pick your tool with intention, and don’t be afraid to swap models mid-stream.

In 2025 we’ve been spoiled with a variety of capable code-focused LLMs. Part of my workflow is choosing the model or service best suited to each task. Sometimes it can be valuable to even try two or more LLMs in parallel to cross-check how they might approach the same problem differently.

Each model has its own “personality”. The key is: if one model gets stuck or gives mediocre outputs, try another. I’ve literally copied the same prompt from one chat into another service to see if it can handle it better. This “model musical chairs” can rescue you when you hit a model’s blind spot.

Also, make sure you’re using the best version available. If you can, use the newest “pro” tier models — because quality matters. And yes, it often means paying for access, but the productivity gains can justify it. Ultimately, pick the AI pair programmer whose “vibe” meshes with you. I know folks who prefer one model simply because they like how its responses feel. That’s valid — when you’re essentially in a constant dialogue with an AI, the UX and tone make a difference.

Personally I gravitate towards Gemini for a lot of coding work these days because the interaction feels more natural and it often understands my requests on the first try. But I will not hesitate to switch to another model if needed; sometimes a second opinion helps the solution emerge. In summary: use the best tool for the job, and remember you have an arsenal of AIs at your disposal.
Leverage AI coding across the lifecycle

Supercharge your workflow with coding-specific AI help across the SDLC.

On the command-line, new AI agents emerged. Claude Code, OpenAI’s Codex CLI and Google’s Gemini CLI are CLI tools where you can chat with them directly in your project directory — they can read files, run tests, and even multi-step fix issues. I’ve used Google’s Jules and GitHub’s Copilot Agent as well — these are asynchronous coding agents that actually clone your repo into a cloud VM and work on tasks in the background (writing tests, fixing bugs, then opening a PR for you). It’s a bit eerie to witness: you issue a command like “refactor the payment module for X” and a little while later you get a pull request with code changes and passing tests. We are truly living in the future. You can read more about this in conductors to orchestrators.

That said, these tools are not infallible, and you must understand their limits. They accelerate the mechanical parts of coding — generating boilerplate, applying repetitive changes, running tests automatically — but they still benefit greatly from your guidance. For instance, when I use an agent like Claude or Copilot to implement something, I often supply it with the plan or to-do list from earlier steps so it knows the exact sequence of tasks. If the agent supports it, I’ll load up my spec.md or plan.md in the context before telling it to execute. This keeps it on track.

We’re not at the stage of letting an AI agent code an entire feature unattended and expecting perfect results. Instead, I use these tools in a supervised way: I’ll let them generate and even run code, but I keep an eye on each step, ready to step in when something looks off. There are also orchestration tools like Conductor that let you run multiple agents in parallel on different tasks (essentially a way to scale up AI help) — some engineers are experimenting with running 3–4 agents at once on separate features. I’ve dabbled in this “massively parallel” approach; it’s surprisingly effective at getting a lot done quickly, but it’s also mentally taxing to monitor multiple AI threads! For most cases, I stick to one main agent at a time and maybe a secondary one for reviews (discussed below).

Just remember these are power tools — you still control the trigger and guide the outcome.
Press enter or click to view image in full size

A full overview of where AI can improve the developer experience. This spans design, inner, submit, and outer loops — highlighting every point where AI can meaningfully reduce toil.
Keep a human in the loop — verify, test, and review everything

AI will happily produce plausible-looking code, but you are responsible for quality — always review and test thoroughly. One of my cardinal rules is never to blindly trust an LLM’s output. As Simon Willison aptly says, think of an LLM pair programmer as “over-confident and prone to mistakes”. It writes code with complete conviction — including bugs or nonsense — and won’t tell you something is wrong unless you catch it. So I treat every AI-generated snippet as if it came from a junior developer: I read through the code, run it, and test it as needed. You absolutely have to test what it writes — run those unit tests, or manually exercise the feature, to ensure it does what it claims. Read more about this in vibe coding is not an excuse for low-quality work.

In fact, I weave testing into the workflow itself. My earlier planning stage often includes generating a list of tests or a testing plan for each step. If I’m using a tool like Claude Code, I’ll instruct it to run the test suite after implementing a task, and have it debug failures if any occur. This kind of tight feedback loop (write code → run tests → fix) is something AI excels at as long as the tests exist. It’s no surprise that those who get the most out of coding agents tend to be those with strong testing practices. An agent like Claude can “fly” through a project with a good test suite as safety net. Without tests, the agent might blithely assume everything is fine (“sure, all good!”) when in reality it’s broken several things. So, invest in tests — it amplifies the AI’s usefulness and confidence in the result.

Even beyond automated tests, do code reviews — both manual and AI-assisted. I routinely pause and review the code that’s been generated so far, line by line. Sometimes I’ll spawn a second AI session (or a different model) and ask it to critique or review code produced by the first. For example, I might have Claude write the code and then ask Gemini, “Can you review this function for any errors or improvements?” This can catch subtle issues. The key is to not skip the review just because an AI wrote the code. If anything, AI-written code needs extra scrutiny, because it can sometimes be superficially convincing while hiding flaws that a human might not immediately notice.

I also use Chrome DevTools MCP, built with my last team, for my debugging and quality loop to bridge the gap between static code analysis and live browser execution. It “gives your agent eyes”. It lets me grant my AI tools direct access to see what the browser can, inspect the DOM, get rich performance traces, console logs or network traces. This integration eliminates the friction of manual context switching, allowing for automated UI testing directly through the LLM. It means bugs can be diagnosed and fixed with high precision based on actual runtime data.

The dire consequences of skipping human oversight have been documented. One developer who leaned heavily on AI generation for a rush project described the result as an inconsistent mess — duplicate logic, mismatched method names, no coherent architecture. He realized he’d been “building, building, building” without stepping back to really see what the AI had woven together. The fix was a painful refactor and a vow to never let things get that far out of hand again. I’ve taken that to heart. No matter how much AI I use, I remain the accountable engineer.

In practical terms, that means I only merge or ship code after I’ve understood it. If the AI generates something convoluted, I’ll ask it to add comments explaining it, or I’ll rewrite it in simpler terms. If something doesn’t feel right, I dig in — just as I would if a human colleague contributed code that raised red flags.

It’s all about mindset: the LLM is an assistant, not an autonomously reliable coder. I am the senior dev; the LLM is there to accelerate me, not replace my judgment. Maintaining this stance not only results in better code, it also protects your own growth as a developer. (I’ve heard some express concern that relying too much on AI might dull their skills — I think as long as you stay in the loop, actively reviewing and understanding everything, you’re still sharpening your instincts, just at a higher velocity.) In short: stay alert, test often, review always. It’s still your codebase at the end of the day.
Press enter or click to view image in full size
Commit often and use version control as a safety net. Never commit code you can’t explain.

Frequent commits are your save points — they let you undo AI missteps and understand changes.

When working with an AI that can generate a lot of code quickly, it’s easy for things to veer off course. I mitigate this by adopting ultra-granular version control habits. I commit early and often, even more than I would in normal hand-coding. After each small task or each successful automated edit, I’ll make a git commit with a clear message. This way, if the AI’s next suggestion introduces a bug or a messy change, I have a recent checkpoint to revert to (or cherry-pick from) without losing hours of work. One practitioner likened it to treating commits as “save points in a game” — if an LLM session goes sideways, you can always roll back to the last stable commit. I’ve found that advice incredibly useful. It’s much less stressful to experiment with a bold AI refactor when you know you can undo it with a git reset if needed.

Proper version control also helps when collaborating with the AI. Since I can’t rely on the AI to remember everything it’s done (context window limitations, etc.), the git history becomes a valuable log. I often scan my recent commits to brief the AI (or myself) on what changed. In fact, LLMs themselves can leverage your commit history if you provide it — I’ve pasted git diffs or commit logs into the prompt so the AI knows what code is new or what the previous state was. Amusingly, LLMs are really good at parsing diffs and using tools like git bisect to find where a bug was introduced. They have infinite patience to traverse commit histories, which can augment your debugging. But this only works if you have a tidy commit history to begin with.

Another benefit: small commits with good messages essentially document the development process, which helps when doing code review (AI or human). If an AI agent made five changes in one go and something broke, having those changes in separate commits makes it easier to pinpoint which commit caused the issue. If everything is in one giant commit titled “AI changes”, good luck! So I discipline myself: finish task, run tests, commit. This also meshes well with the earlier tip about breaking work into small chunks — each chunk ends up as its own commit or PR.

Finally, don’t be afraid to use branches or worktrees to isolate AI experiments. One advanced workflow I’ve adopted (inspired by folks like Jesse Vincent) is to spin up a fresh git worktree for a new feature or sub-project. This lets me run multiple AI coding sessions in parallel on the same repo without them interfering, and I can later merge the changes. It’s a bit like having each AI task in its own sandbox branch. If one experiment fails, I throw away that worktree and nothing is lost in main. If it succeeds, I merge it in. This approach has been crucial when I’m, say, letting an AI implement Feature A while I (or another AI) work on Feature B simultaneously. Version control is what makes this coordination possible. In short: commit often, organize your work with branches, and embrace git as the control mechanism to keep AI-generated changes manageable and reversible.
Press enter or click to view image in full size
Customize the AI’s behavior with rules and examples

Steer your AI assistant by providing style guides, examples, and even “rules files” — a little upfront tuning yields much better outputs.

One thing I learned is that you don’t have to accept the AI’s default style or approach — you can influence it heavily by giving it guidelines. For instance, I have a CLAUDE.md file that I update periodically, which contains process rules and preferences for Claude (Anthropic’s model) to follow (and similarly a GEMINI.md when using Gemini CLI). This includes things like “write code in our project’s style, follow our lint rules, don’t use certain functions, prefer functional style over OOP,” etc. When I start a session, I feed this file to Claude to align it with our conventions. It’s surprising how well this works to keep the model “on track” as Jesse Vincent noted — it reduces the tendency of the AI to go off-script or introduce patterns we don’t want.

Even without a fancy rules file, you can set the tone with custom instructions or system prompts. GitHub Copilot and Cursor both introduced features to let you configure the AI’s behavior globally for your project. I’ve taken advantage of that by writing a short paragraph about our coding style, e.g. “Use 4 spaces indent, avoid arrow functions in React, prefer descriptive variable names, code should pass ESLint.” With those instructions in place, the AI’s suggestions adhere much more closely to what a human teammate might write. Ben Congdon mentioned how shocked he was that few people use Copilot’s custom instructions, given how effective they are — he could guide the AI to output code matching his team’s idioms by providing some examples and preferences upfront. I echo that: take the time to teach the AI your expectations.

Another powerful technique is providing in-line examples of the output format or approach you want. If I want the AI to write a function in a very specific way, I might first show it a similar function already in the codebase: “Here’s how we implemented X, use a similar approach for Y.” If I want a certain commenting style, I might write a comment myself and ask the AI to continue in that style. Essentially, prime the model with the pattern to follow. LLMs are great at mimicry — show them one or two examples and they’ll continue in that vein.

The community has also come up with creative “rulesets” to tame LLM behavior. You might have heard of the “Big Daddy” rule or adding a “no hallucination/no deception” clause to prompts. These are basically tricks to remind the AI to be truthful and not overly fabricate code that doesn’t exist. For example, I sometimes prepend a prompt with: “If you are unsure about something or the codebase context is missing, ask for clarification rather than making up an answer.” This reduces hallucinations. Another rule I use is: “Always explain your reasoning briefly in comments when fixing a bug.” This way, when the AI generates a fix, it will also leave a comment like “// Fixed: Changed X to Y to prevent Z (as per spec).” That’s super useful for later review.

In summary, don’t treat the AI as a black box — tune it. By configuring system instructions, sharing project docs, or writing down explicit rules, you turn the AI into a more specialized developer on your team. It’s akin to onboarding a new hire: you’d give them the style guide and some starter tips, right? Do the same for your AI pair programmer. The return on investment is huge: you get outputs that need less tweaking and integrate more smoothly with your codebase.
Embrace testing and automation as force multipliers

Use your CI/CD, linters, and code review bots — AI will work best in an environment that catches mistakes automatically.

This is a corollary to staying in the loop and providing context: a well-oiled development pipeline enhances AI productivity. I ensure that any repository where I use heavy AI coding has a robust continuous integration setup. That means automated tests run on every commit or PR, code style checks (like ESLint, Prettier, etc.) are enforced, and ideally a staging deployment is available for any new branch. Why? Because I can let the AI trigger these and evaluate the results. For instance, if the AI opens a pull request via a tool like Jules or GitHub Copilot Agent, our CI will run tests and report failures. I can feed those failure logs back to the AI: “The integration tests failed with XYZ, let’s debug this.” It turns bug-fixing into a collaborative loop with quick feedback, which AIs handle quite well (they’ll suggest a fix, we run CI again, and iterate).

Automated code quality checks (linters, type checkers) also guide the AI. I actually include linter output in the prompt sometimes. If the AI writes code that doesn’t pass our linter, I’ll copy the linter errors into the chat and say “please address these issues.” The model then knows exactly what to do. It’s like having a strict teacher looking over the AI’s shoulder. In my experience, once the AI is aware of a tool’s output (like a failing test or a lint warning), it will try very hard to correct it — after all, it “wants” to produce the right answer. This ties back to providing context: give the AI the results of its actions in the environment (test failures, etc.) and it will learn from them.

AI coding agents themselves are increasingly incorporating automation hooks. Some agents will refuse to say a code task is “done” until all tests pass, which is exactly the diligence you want. Code review bots (AI or otherwise) act as another filter — I treat their feedback as additional prompts for improvement. For example, if CodeRabbit or another reviewer comments “This function is doing X which is not ideal” I will ask the AI, “Can you refactor based on this feedback?”

By combining AI with automation, you start to get a virtuous cycle. The AI writes code, the automated tools catch issues, the AI fixes them, and so forth, with you overseeing the high-level direction. It feels like having an extremely fast junior dev whose work is instantly checked by a tireless QA engineer. But remember, you set up that environment. If your project lacks tests or any automated checks, the AI’s work may slip through with subtle bugs or poor quality until much later.

So as we head into 2026, one of my goals is to bolster the quality gates around AI code contribution: more tests, more monitoring, perhaps even AI-on-AI code reviews. It might sound paradoxical (AIs reviewing AIs), but I’ve seen it catch things one model missed. Bottom line: an AI-friendly workflow is one with strong automation — use those tools to keep the AI honest.
Press enter or click to view image in full size
Continuously learn and adapt (AI amplifies your skills)

Treat every AI coding session as a learning opportunity — the more you know, the more the AI can help you, creating a virtuous cycle.

One of the most exciting aspects of using LLMs in development is how much I have learned in the process. Rather than replacing my need to know things, AIs have actually exposed me to new languages, frameworks, and techniques I might not have tried on my own.

This pattern holds generally: if you come to the table with solid software engineering fundamentals, the AI will amplify your productivity multifold. If you lack that foundation, the AI might just amplify confusion. Seasoned devs have observed that LLMs “reward existing best practices” — things like writing clear specs, having good tests, doing code reviews, etc., all become even more powerful when an AI is involved. In my experience, the AI lets me operate at a higher level of abstraction (focusing on design, interface, architecture) while it churns out the boilerplate, but I need to have those high-level skills first. As Simon Willison notes, almost everything that makes someone a senior engineer (designing systems, managing complexity, knowing what to automate vs hand-code) is what now yields the best outcomes with AI. So using AIs has actually pushed me to up my engineering game — I’m more rigorous about planning and more conscious of architecture, because I’m effectively “managing” a very fast but somewhat naïve coder (the AI).

For those worried that using AI might degrade their abilities: I’d argue the opposite, if done right. By reviewing AI code, I’ve been exposed to new idioms and solutions. By debugging AI mistakes, I’ve deepened my understanding of the language and problem domain. I often ask the AI to explain its code or the rationale behind a fix — kind of like constantly interviewing a candidate about their code — and I pick up insights from its answers. I also use AI as a research assistant: if I’m not sure about a library or approach, I’ll ask it to enumerate options or compare trade-offs. It’s like having an encyclopedic mentor on call. All of this has made me a more knowledgeable programmer.

The big picture is that AI tools amplify your expertise. Going into 2026, I’m not afraid of them “taking my job” — I’m excited that they free me from drudgery and allow me to spend more time on creative and complex aspects of software engineering. But I’m also aware that for those without a solid base, AI can lead to Dunning-Kruger on steroids (it may seem like you built something great, until it falls apart). So my advice: continue honing your craft, and use the AI to accelerate that process. Be intentional about periodically coding without AI too, to keep your raw skills sharp. In the end, the developer + AI duo is far more powerful than either alone, and the developer half of that duo has to hold up their end.
Press enter or click to view image in full size
Conclusion

As we enter 2026, I’ve fully embraced AI in my development workflow — but in a considered, expert-driven way. My approach is essentially “AI-augmented software engineering” rather than AI-automated software engineering.

I’ve learned: the best results come when you apply classic software engineering discipline to your AI collaborations. It turns out all our hard-earned practices — design before coding, write tests, use version control, maintain standards — not only still apply, but are even more important when an AI is writing half your code.

I’m excited for what’s next. The tools keep improving and my workflow will surely evolve alongside them. Perhaps fully autonomous “AI dev interns” will tackle more grunt work while we focus on higher-level tasks. Perhaps new paradigms of debugging and code exploration will emerge. No matter what, I plan to stay in the loop — guiding the AIs, learning from them, and amplifying my productivity responsibly.

The bottom line for me: AI coding assistants are incredible force multipliers, but the human engineer remains the director of the show.

With that…happy building in 2026! 🚀

I’m excited to share I’ve released a new AI-assisted engineering book with O’Reilly. There are a number of free tips on the book site in case interested.
Programming
AI
Coding
Vibe Coding
Software Engineering

Addy Osmani
Written by Addy Osmani
86K followers
·
871 following

Director, Google Cloud AI - Gemini, Vertex, Agents
Responses (5)

Write a response

What are your thoughts?
Kwirth

Kwirth

Feb 18

LLMs are only as good as the context you provide — show them the relevant code, docs, and constraints.

Agreed. The whole key is shared context. But, what is the best way to iterate on the context with the coding agent. I believe it is visual. The human should see what the AI is changing, collaborate on the context... for instance in a markdown doc…

Denis Petelin

Denis Petelin

Feb 3

It seems like Mimir will serve your workflow just fine, both the flow and the skills part: https://github.com/phainestai/mimir#

Dmitry Sky

Dmitry Sky

Jan 13

On the command-line, new AI agents emerged. Claude Code, OpenAI’s Codex CLI and Google’s Gemini CLI are CLI tools where you can chat with them directly in your project directory — they ...

This is beyond redundant. If you already use Cursor, you get the same models, deeper IDE context, parallel local agents via worktrees, tighter control and faster feedback. For hands-on, local, supervised development, Cursor alone is beyond sufficient for 99% of developers.

More from Addy Osmani
Vibe coding is not the same as AI-Assisted engineering.
Addy Osmani

Addy Osmani
Vibe coding is not the same as AI-Assisted engineering.
You can find more of my writing on my Substack and Beyond Vibe Coding.
Nov 30, 2025
104
4
Stop Using /init for AGENTS.md
Addy Osmani

Addy Osmani
Stop Using /init for AGENTS.md
TL;DR: A good mental model is to treat AGENTS.md as a living list of codebase smells you haven’t fixed yet, not a permanent configuration…
Mar 19
84
3
Comprehension Debt — the hidden cost of AI generated code.
Addy Osmani

Addy Osmani
Comprehension Debt — the hidden cost of AI generated code.
Comprehension debt is the hidden cost to human intelligence and memory resulting from excessive reliance on AI and automation. For…
Mar 15
109
4
How modern browsers work
Addy Osmani

Addy Osmani
How modern browsers work
A very deep-dive into how modern web browsers load and render web pages.
Nov 29, 2025
473
7
See all from Addy Osmani
Recommended from Medium
10 Must-Have Skills for Claude (and Any Coding Agent) in 2026
unicodeveloper

unicodeveloper
10 Must-Have Skills for Claude (and Any Coding Agent) in 2026
The definitive guide to agent skills that change how Claude Code, Cursor, Gemini CLI, and other AI coding assistants perform in production.
Mar 9
1K
15
Vibe Coding is Over illustration of three ai generated landing pages with the words IT’S OVER written at the top in large text
Michal Malewicz

Michal Malewicz
Vibe Coding is OVER.
Here’s What Comes Next.
6d ago
1.7K
51
The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work
Bibek Poudel

Bibek Poudel
The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work
If your skill does not trigger, it is almost never the instructions. It is the description.
Feb 26
90
A high-contrast digital graphic with a dark, ethereal blue and purple background. Large, glowing cyan text in the center reads “USING LLMs IS A SKILL.” Below the text are three minimalist neon icons: a stack of books with a quill, a castle tower, and a human brain merged with mechanical gears. Small text at the bottom reads “Based on ‘Learning the Art’ concept.”
Leo Godin

Leo Godin
Claude Code is Great
You Just Need to Learn How to Use It
Mar 2
1.3K
30
Using spec-driven development with Claude Code
Heeki Park

Heeki Park
Using spec-driven development with Claude Code
I no longer write code by hand. I wouldn’t call myself a proper software development engineer by trade, nor have I deployed large-scale…
Mar 1
614
14
The Complete Guide to Claude Code: CLAUDE.md
AI Advances

In

AI Advances

by

zhaozhiming
The Complete Guide to Claude Code: CLAUDE.md
A comprehensive guide to the CLAUDE.md file in Claude Code, including how it is loaded, how to write it, best practices, and how it…
Mar 17
925
8
See more recommendations

Help

Status

About

Careers

Press

Blog

Privacy

Rules

Terms

Text to speech

Best Practices for Creating Agent Skills

This guide explains how to write professional-grade skills for agents, validate them using LLMs, and maintain a lean context window.

This guide is a concentrated set of best practices for creating agent skills. If you're looking for a comprehensive documentation see Claude's docs.

To evaluate if your skills do well and prevent regressions, check out [skillgrade]((https://github.com/mgechev/skillgrade).
Structure of a skill

Every skill must follow this directory structure:

Plaintext

skill-name/
├── SKILL.md              # Required: Metadata + core instructions (<500 lines)
├── scripts/              # Executable code (Python/Bash) designed as tiny CLIs
├── references/           # Supplementary context (schemas, cheatsheets) 
└── assets/               # Templates or static files used in output

    SKILL.md: Acts as the "brain." Use it for navigation and high-level procedures.
    References: Link directly from SKILL.md. Keep them one level deep only.
    Scripts: Use for fragile/repetitive operations where variation is a bug. Do not bundle library code here;

Optimize the frontmatter for discoverability

The name and description in the frontmatter of your SKILL.md are the only fields that the agent sees before triggering a skill. If they are not optimized for discoverability and specific enough, your skill is invisible.

    Adhere to Strict Naming: The name field must be 1-64 characters, contain only lowercase letters, numbers, and hyphens (no consecutive hyphens), and must exactly match the parent directory name (e.g., name: angular-testing must live in angular-testing/SKILL.md).
    Write Trigger-Optimized Descriptions: (Max 1,024 characters). This is the only metadata the agent sees for routing. Describe the capability in the third person and include "negative triggers."
        Bad: "React skills." (Too vague).
        Good: "Creates and builds React components using Tailwind CSS. Use when the user wants to update component styles or UI logic. Don't use it for Vue, Svelte, or vanilla CSS projects."

Progressive disclosure and resource management

Maintain a pristine context window by loading information only when needed. SKILL.md is the "brain" for high-level logic; offload details to subdirectories.

    Keep SKILL.md Lean: Limit the main file to <500 lines. Use it for navigation and primary procedures.
    Use Flat Subdirectories: Move bulky context to standard folders. Keep files exactly one level deep (e.g., references/schema.md, not references/db/v1/schema.md).
        references/: API docs, cheatsheets, domain logic.
        scripts/: Executable code for deterministic tasks.
        assets/: Output templates, JSON schemas, images.
    Just-in-Time (JiT) Loading: Explicitly instruct the agent when to read a file. It will not see these resources until you direct it to (e.g., "See references/auth-flow.md for specific error codes").
    Explicit Pathing: Always use relative paths with forward slashes (/), regardless of the OS.

Skills are for agents, not humans. To keep the context window lean and avoid unnecessary token consumption. Do not create:

    Documentation files: README.md, CHANGELOG.md, or INSTALLATION_GUIDE.md.
    Redundant logic: If the agent already handles a task reliably without help, delete the instruction.
    Library code: Skills should reference existing tools or contain tiny, single-purpose scripts. Long-lived library code belongs in standard repo CLI directories.

Use specific procedural instructions instead of prose

Create instructions for LLMs instead of humans.

    Use Step-by-Step Numbering: Define the workflow as a strict chronological sequence. If there is a decision tree, map it out clearly (e.g., "Step 2: If you need source maps run ng build --source-map. Otherwise, skip to Step 3.").
    Provide Concrete Templates: Agents pattern-match exceptionally well. Instead of spending paragraphs describing how a JSON output should look, place a template in the assets/ folder and instruct the agent to copy its structure.
    Write in the Third-Person Imperative: Frame instructions as direct commands to the agent (e.g., "Extract the text..." rather than "I will extract..." or "You should extract...").

Be specific and consistent in the way you reference concepts in your skill files.

    Use identical terminology: Pick a single term to refer to a specific concept.
    Specificity: Use the most specific terminology that’s native to the domain that you describe. For example, in Angular use the concept “template” instead of “html”, “markup”, or “view”.

Bundle deterministic scripts for repetitive operations

Don't ask the LLM to write complex parsing logic or boilerplate code from scratch every time it runs a skill.

    Offload fragile/repetitive tasks: If the agent needs to parse a complex dataset or query a specific database, give it a tested Python, Bash, or Node script to run in the scripts/ directory.
    Handle edge cases gracefully: An agent relies on standard output (stdout/stderr) to know if a script succeeded. Write scripts that return highly descriptive, human-readable error messages so the agent knows exactly how to self-correct without needing user intervention.

Validation Guide

Since LLMs will be using your skills, the best way I’ve identified to ensure they are useful is in collaboration with LLMs.

It’s critical to have evals for your skills to make sure the changes you’re making have a positive impact and don’t lead to regression. A popular benchmark for skills is SkillsBench which could help with some inspiration.

Once you draft the initial version of your skills, you can validate your work going through the following steps:
Discovery Validation

Agents load skills based strictly on the YAML frontmatter. Test how an LLM interprets your description in isolation to prevent false triggers (like firing for a React app when it's meant for Angular).

Paste exactly the text below into a fresh LLM chat:

    I am building an Agent Skill based on the agentskills.io spec. Agents will decide whether to load this skill based entirely on the YAML metadata below.

    name: angular-vite-migrator
    description: Migrates Angular CLI projects from Webpack to Vite and esbuild. Use when the user wants to update builder configurations, replace webpack plugins with rollup equivalents, or speed up Angular compilation.

    Based strictly on this description:

        Generate 3 realistic user prompts that you are 100% confident should trigger this skill.
        Generate 3 user prompts that sound similar but should NOT trigger this skill (e.g., migrating a React app to Vite, or just updating Angular versions).
        Critique the description: Is it too broad? Suggest an optimized rewrite.

In addition, prompt agents with assignments that you expect to trigger a skill read and inspect the thought process. Go back and forth with the agent to identify why it picked (or didn’t) particular skills.
Logic Validation

Ensure your step-by-step instructions are deterministic and don't force the agent to hallucinate missing steps.

Feed the LLM your entire SKILL.md and directory structure:

    Here is the full draft of my SKILL.md and the directory tree of its supporting files.

    ├── SKILL.md
    ├── scripts/esbuild-optimizer.mjs
    └── assets/vite.config.template.ts

    [Paste your SKILL.md contents here] Act as an autonomous agent that has just triggered this skill. Simulate your execution step-by-step based on a request to Migrate my Angular v17 app to Vite.

    For each step, write out your internal monologue:

        What exactly are you doing?
        Which specific file/script are you reading or running?
        Flag any Execution Blockers: Point out the exact line where you are forced to guess or hallucinate because my instructions are ambiguous (e.g., how to map Angular environment files to Vite's import.meta.env).

Edge Case Testing

Force the LLM to hunt for vulnerabilities, unsupported configurations, and failure states inherent to web tooling.

Ask the LLM to attack your logic:

    Now, switch roles. Act as a ruthless QA tester. Your goal is to break this skill. Ask me 3 to 5 highly specific, challenging questions about edge cases, failure states, or missing fallbacks in the SKILL.md. Focus on:

        What if scripts/esbuild-optimizer.mjs fails due to a legacy CommonJS dependency?
        What if the user's angular.json contains heavily customized Webpack builders (@angular-builders/custom-webpack) that Vite doesn't support?
        Are there implicit assumptions I made about the user's Node environment?

    Do not fix these issues yet. Just ask me the numbered questions and wait for me to answer them.

Architecture Refinement

LLMs often try to stuff large config files directly into the main prompt. Use this step to enforce progressive disclosure and shrink the token footprint.

Have the LLM apply your fixes and restructure the skill:

    Based on my answers to your edge-case questions, rewrite the SKILL.md file, strictly enforcing the Progressive Disclosure design pattern:

        Keep the main SKILL.md strictly as a high-level set of steps using third-person imperative commands (e.g., Execute the esbuild script, Read the Vite config template).
        If there are dense rules, large vite.config.ts templates, or complex angular.json schemas currently in the file, remove them. Tell me to create a new file in references/ or assets/, and replace the text in SKILL.md with a strict command to read that specific file only when needed.
        Add a dedicated Error Handling section at the bottom incorporating my answers about Webpack fallbacks and CommonJS resolution.


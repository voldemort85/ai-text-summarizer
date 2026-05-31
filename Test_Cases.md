# AI Text Summarizer - Test Cases

## Overview

This document contains the functional test cases used to validate the AI Text Summarizer application.

### Preconditions

* Application is running successfully.
* User has access to the Gradio interface.
* DistilBART model is loaded correctly.

## Functional Test Cases

| TC ID | Scenario                              | Input                                       | Expected Result                                             | Status |
| ----- | ------------------------------------- | ------------------------------------------- | ----------------------------------------------------------- | ------ |
| TC-01 | Valid long text with default option   | 50+ word paragraph, Summary Type = Medium   | Summary generated successfully                              | Pass   |
| TC-02 | Valid long text with Short summary    | 50+ word paragraph, Summary Type = Short    | Short summary generated                                     | Pass   |
| TC-03 | Valid long text with Detailed summary | 50+ word paragraph, Summary Type = Detailed | Detailed summary generated                                  | Pass   |
| TC-04 | Input below minimum word count        | 29 words                                    | Validation message displayed                                | Pass   |
| TC-05 | Boundary condition                    | Exactly 30 words                            | Summarization proceeds                                      | Pass   |
| TC-06 | Empty input                           | Blank textbox                               | Validation message displayed                                | Pass   |
| TC-07 | Whitespace-only input                 | Spaces/newlines only                        | Validation message displayed                                | Pass   |
| TC-08 | Long article input                    | Large article/document                      | Summary generated without application crash                 | Pass   |
| TC-09 | Default dropdown value                | Open application                            | Medium selected by default                                  | Pass   |
| TC-10 | Dropdown options                      | Open dropdown menu                          | Short, Medium, Detailed available                           | Pass   |
| TC-11 | Multiple paragraphs                   | Multi-paragraph article                     | Summary generated successfully                              | Pass   |
| TC-12 | Content quality                       | Coherent 100+ word article                  | Summary preserves main idea and is shorter than source text | Pass   |

## UI Validation

| Check                 | Expected Result            | Status |
| --------------------- | -------------------------- | ------ |
| Application Title     | AI Text Summarizer         | Pass   |
| Input Textbox         | Visible and editable       | Pass   |
| Summary Type Dropdown | Visible and functional     | Pass   |
| Output Textbox        | Displays generated summary | Pass   |

## Known Limitations

* The DistilBART model performs best on longer text inputs.
* Very short inputs may not produce meaningful summaries.
* Extremely large documents may require text chunking for optimal performance.

## Future Testing Enhancements

* PDF upload testing
* Performance benchmarking
* Large document chunking validation
* API testing (React/FastAPI version)

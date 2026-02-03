# Design de Software

## Worksheet 5

### 2. According to the Software Engineering Institute, the software architecture of a system is the set of structures needed to reason about that system. These structures encompass software elements, their relationships, and properties of both. Consider the diagrams below, related to a system that analyzes a stream of images received from a space probe. The system continuously reads images, applies various processing algorithms to each image to determine if it is interesting, and saves it if that is the case

#### a. What structure or structures are described in each of the diagrams? For each structure, identify the elements, relationships, and properties represented

> A - represents a module view, where modules are the primary elements and the "is-part-of" relationship defines how they are organized into a hierarchy.
> B - represents a UML class diagram, where classes are the primary elements and associations define relationships between them.

#### b. Indicate the decisions expressed in each of the diagrams
>
> A - there are dependencies between modules, indicating that one module relies on another for functionality or data.
>
> B - there are associations between classes, indicating that instances of one class are connected to instances of another class.

#### c. Provide examples of quality attributes affected by the decisions expressed in diagram A
>
>A - Modularity and simplicity are emphasized, as the hierarchical structure allows for clear organization and separation of concerns.

#### d. What properties of the ImageAnalysis#n elements could be important for analyzing reliability-related properties in detecting the “interest” of an image?
>
>

#### e. Indicate, justifying, another important view for analyzing properties related to system performance (e.g., throughput and latency)
>
>

### 3. The MediaPlayer is a multimedia system that, when connected to a sound system and a television, is used to view photos and movies, and listen to music. The system supports different formats, and resources can be read either from the system's hard drive or received via streaming from the internet. This system is detailed in the book “Just Enough Software Architecture” by G. Fairbanks

### The system, still in a prototype version, was built from scratch. All team members who developed the system participated in design decisions, understand its architecture and detailed design, but all this information exists only in their minds. With the project being successful, the company is planning to launch the product by the end of the year

#### a. Imagine that you are asked to document the architecture of the embedded software system in MediaPlayer. To perform this task, you have several alternatives, some listed below. Which alternatives would you choose and in what order? Justify

- Analyze the source code of the system to see how it was built.
- Analyze the functional requirements of the system to understand what the
system is supposed to do.
- Analyse the implemented functionalities to see what the system actually
does.
- Talk to the people who developed the system to understand the decisions
they made and why.

> Firstly to quickly document the software, one must first analyse the functional requirements of the system to know what it is supposed to do. Then, analyse the functionalities implemented to see what it actually does. After that, talk to the developers to understand the design decisions made, and finally, analyze the source code to fill in any gaps and ensure accuracy. This order helps in building a starting point from requirements to implementation, ensuring stakeholders are considered before delving into technical details.

#### b. Please provide at least 2 reasons that justify dedicating time to the recovery and documentation of the MediaPlayer architecture, knowing that the system exists, and the project was successful
>
> With the success of the project comes maintenance and possible new features. As such, having a good documentation is key to quickly understand the system and be able to make changes without breaking existing functionality. Furthermore, good documentation helps onboard new developers faster, as they can refer to it to understand the system's architecture and design decisions.

#### c. The system's source code is organized in the file system in various directories as shown in the figure. Can you assume that each directory corresponds to a module of the system? Why?
>
> No, the organization of source code in directories does not necessarily correspond to modules of the system. Directories may be organized based on various factors such as functionality, feature sets, or even developer preferences, which may not align with the modular structure of the software. Modules are defined by their responsibilities and interactions, which may span multiple directories or be contained within a single directory.

#### d. The team responsible for the recovery and documentation of the system architecture produced the view presented below. What does this view describe? Provide 3 examples of the types of dependencies the diagram refers to, and at least 3 reasons why this view is useful
>
>

#### e. Provide 2 examples of architectural decisions that respect the module view and cannot be extracted from the source code
>
>

#### f. The team responsible for the recovery and documentation of the system architecture retrieved the quality attributes that were considered in the system's design, along with their priority

- i. UI responsiveness (latency)
- ii. Smoothness of Audio/Video playback (consistent and timely)
- iii. Reliability
- iv. Modifiability, particularly regarding different video sources and codecs
- v. Efficiency in playback (framerate)
- vi. Portability

#### Identify, justifying, pairs of conflicting qualities that may have had to undergo compromises (tradeoffs) during the design of the system architecture
>
>

#### g. The team responsible for the recovery and documentation of the system architecture also included the view presented below in the SAD. What decisions does this view describe?
>
>

#### h. Part of the documentation for this view includes the following information

#### Try to relate the decisions expressed in this architectural view to the quality attributes that were declared to have been considered

#### i. In the same architectural view, the way components collaborate in a specific scenario was documented. What is the usefulness of this description? What reasons can justify describing a specific scenario instead of a complete model of the behavior for the actions of different use cases?
>
>

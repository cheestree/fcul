# Design de Software

## Worksheet 3

### 1. Consider the statement "Fitness of purpose doesn’t provide an absolute measure of quality"

#### a. Does this statement apply to software design? Justify

> It does, as software quality can be assessed through many other metrics besides the purpose of the software. For example, maintainability, usability, performance, and security are all important aspects of software quality that may not directly relate to the software's intended purpose.

##### b. Consider an inkjet printer, a device with embedded software. Identify what corresponds to fitness for purpose in this case and give examples of other quality measures that may be relevant in this case

> An inkjet printer prints, but it can also scan and copy documents. While its primary purpose is printing, its quality can also be evaluated based on its scanning and copying capabilities. Other factors such as print quality, speed, and reliability also contribute to its overall quality.

### 2. Quality concepts

#### a. Reliability is one of the most widely applicable quality concepts to software systems. How does reliability relate to the concept of robustness?

> Reliability refers to the ability of software to perform its intended functions consistently over time without failures. A robust system is designed to handle unexpected conditions and continue operating correctly, even in the face of errors or adverse situations.

#### b. Time to market is also a quality concept

##### i. Explain why this concept is potentially conflicting with the previous one

>A robust solution might take more time to develop as it requires thorough testing and consideration of various failure scenarios. Time to market, on the other hand, focuses on delivering a product quickly, which may lead to compromises in robustness.

##### ii. Name two types of software systems in which the relative importance given to each of these concepts is very different

> Social media applications often prioritize time to market to quickly capture user interest, while safety-critical systems, such as medical devices, prioritize robustness to ensure reliability and safety.

#### c. Modifiability and performance are yet two other quality concepts applicable to most software systems

##### i. Why are these two concepts of different types?

> Modifiability is the ease with which software can be changed to correct faults, improve performance, or adapt to a changed environment. Performance refers to how efficiently software uses resources and responds to user inputs. They are of different types because modifiability is a quality attribute related to the software's structure and design, while performance is a measure of how well the software operates.

##### ii. Explain why these concepts are potentially conflicting
>
> They are conflicting because improving modifiability often involves adding layers of abstraction or modularity, which can introduce overhead and reduce performance. Conversely, optimizing for performance may lead to more rigid designs that are harder to modify.

##### iii. Two code fragments are considered clones if they are structurally similar. Indicate, justifying, to what extent a metric measuring the quantity of clones in a software system's code can be used to evaluate its modifiability (what can be concluded if there is a high number of clones? and if there is a very low number of clones?)
>
>If there's a low quantity of cloned code, maintainability may not be significantly affected, as the codebase remains easier to understand and modify. However, if cloned code is prevalent, it can lead to increased maintenance efforts, as changes need to be replicated across multiple locations, increasing the risk of inconsistencies and errors.

#### d. Usability is another quality concept applicable to the majority of software systems. Consider the following excerpt from the book "Software Architecture in Practice"
>
> "Making the interface clear and easy to use is primarily a matter of getting the details correct (…) although these details matter tremendously to the end user and influence usability, they are almost always encapsulated within a single component."

##### i. Indicate, justifying, which quality concepts are being prioritized when deciding to have interface details encapsulated in a single component
>
> Having interface details in a single component can improve usability by providing a clear and consistent point of interaction for users. However, it may reduce modifiability, as changes to the interface may require modifications to the single component, potentially affecting other parts of the system.

##### ii. Provide examples that illustrate there may be conflicts between usability requirements and requirements related to other qualities. Justify your response

### 3. Simplicity is an important quality attribute for evaluating the designs of a software system

#### a. Explain what it means
>
> Simplicity in software design refers to the practice of keeping the design as straightforward and uncomplicated as possible. This involves minimizing complexity, avoiding unnecessary features, and ensuring that the software is easy to understand, maintain, and use.

#### b. Indicate, justifying, the quality concepts of software systems directly related to the simplicity of their designs
>
> Simplicity directly affects maintainability, as simpler designs are easier to understand and modify. It can also enhance usability, as users find it easier to navigate and interact with straightforward interfaces. However, simplicity may sometimes conflict with performance, as optimizing for speed or resource usage can introduce complexity.

#### c. Identify at least two metrics that can be used to evaluate the simplicity of a design and that address the simplicity of different structures. Identify the type of structure they focus on
>
> To evaluate simplicity, one could use metrics such as cyclomatic complexity, lines of code, and the number of dependencies. User feedback and usability testing can also provide insights into how simple and intuitive the software is for end-users.

#### d. Specify how tools like the one shown in the figure (CppDepend) below are useful for analysing the simplicity of a design
>
>

#### e. The phenomenon underlying Lehman's Law affects other types of systems. Explain what is different in the case of software systems
>
> Lehman's Law: As an evolving program is continually changed, its complexity, reflecting deteriorating structure, increases unless work is done to maintainor reduce it.
>
> In the case of software systems, Lehman's Law is particularly relevant to large-scale, evolving systems such as enterprise applications or operating systems. These systems must continuously adapt to changing requirements and environments, making them subject to the law's principles of ongoing evolution and complexity management.

#### f. To what extent does the simplicity of a system's design impact Technical Debt? Does it make sense for tools that calculate Technical Debt, such as SQUORE (see the 3 following image), to use metrics that assess simplicity for this purpose? Justify your answer
>
> Simplicity directly impacts technical debt, as simpler designs are easier to maintain and modify, reducing the likelihood of accumulating debt. Complex systems may lead to shortcuts and quick fixes that contribute to technical debt over time.

#### g. In the case of the NDepend tool, as shown in the image below, it is possible to define specific rules for calculating Technical Debt. Analyse what is being defined and whether it makes sense
>
>

### 4. Modularity is another important quality concept for evaluating the designs of a software system

#### a. Explain what it consists of
>
> Modularity is the degree to which a system's components can be separated and recombined. High cohesion refers to how closely related and focused the responsibilities of a single module are, while low coupling refers to the degree of interdependence between modules.

#### b. Indicate, justifying, two quality concepts of software systems directly related to the modularity of their design
>
> Modularity enhances maintainability by allowing developers to work on individual modules without affecting others. High cohesion ensures that modules are focused and easier to understand, while low coupling reduces dependencies, making it easier to change one module without impacting others. It also improves usability by allowing for clearer interfaces and interactions between components.

#### c. Consider the following metric involving the size of a system's modules: SMAX = 1 – (no of modules whose size exceeds MAX / no of modules). Indicate, justifying, whether this metric may, in certain situations, be useful for measuring the modularity of a design. If so, describe these situations and what is the optimal value for SMAX?
>
> The following metric can be used to analyse if there are too many modules in a software system. This metric counts the number of modules in the system and compares it to a predefined threshold based on the system's size and complexity. If the module count exceeds this threshold, it may indicate that the system is overly modularized, leading to increased complexity and maintenance challenges.

#### d. Information Hiding is a technique introduced by David Parnas to design modular structures in a software system. In the context of a questionnaire management application, consisting of questions with multiple-choice options, it is necessary to read and write text files with the questionnaires. Analyse to what extent the decision to have a separate module for reading questionnaires and another for writing them is compatible with Information Hiding
>
>

#### e. Indicate how matrices such as the one shown below—a Design Structure Matrix— can be used to analyse the modularity of a design
>
> A Design Structure Matrix (DSM) is a compact, matrix representation of a system or project that shows the relationships between components or tasks. It can be used to analyze modularity by identifying dependencies and interactions between modules. By examining the DSM, one can identify tightly coupled modules that may need to be decoupled to improve modularity. The matrix can also help in identifying potential areas for refactoring and improving the overall design of the system.

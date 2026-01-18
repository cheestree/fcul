# DS

## Software Development

### Software Development Life Cycle (SDLC)

Planning -> Design -> Coding -> Testing -> Deployment -> Maintenance -> ...

### SDLC Process Models

#### Waterfall Model

A sequential design process where progress flows steadily downward through distinct phases.

Phases:

1. **Requirements**: Gather and document all requirements upfront.
2. **Design**: Create architectural and detailed design based on requirements.
3. **Implementation**: Code the system according to the design.
4. **Verification/Testing**: Test the completed system against requirements.
5. **Deployment**: Release the system to users.
6. **Maintenance**: Fix bugs and make enhancements.

Characteristics:

- Each phase must be completed before the next begins.
- Heavy documentation at each phase.
- Requirements are frozen early.
- Testing happens late in the cycle.

Advantages:

- Simple and easy to understand and use.
- Well-documented process.
- Easy to manage due to rigidity.
- Works well for small projects with well-understood requirements.
- Clear milestones and deliverables.

Disadvantages:

- Inflexible to changing requirements.
- Late discovery of issues (testing at the end).
- High risk and uncertainty.
- Not suitable for complex or object-oriented projects.
- Difficult to go back to previous phases.
- Working software produced late in the cycle.

#### Spiral Model

An iterative risk-driven process model that combines elements of both design and prototyping-in-stages.

Phases (each spiral iteration):

1. **Determine objectives**: Identify objectives, alternatives, and constraints for the iteration.
2. **Risk analysis and mitigation**: Identify and analyze risks, create prototypes to address key risks.
3. **Development and testing**: Develop and verify the product for this iteration.
4. **Plan next iteration**: Review results, plan the next spiral iteration.

Characteristics:

- Combines iterative development with systematic aspects of waterfall.
- Emphasis on risk analysis at each iteration.
- Each spiral produces a more complete version.
- Prototypes used to explore and mitigate risks.
- Suitable for large, complex, expensive projects.

Advantages:

- Risk management is integrated throughout.
- Accommodates changing requirements.
- Early production of working software.
- Suitable for large and complex projects.
- Customer feedback incorporated early and often.
- High amount of risk analysis.

Disadvantages:

- Complex and expensive to manage.
- Requires expertise in risk assessment.
- Success depends heavily on risk analysis phase.
- Not suitable for small projects.
- Can go on indefinitely if not managed properly.
- Extensive documentation required.

### Design process

Design vs Fabrication: while good design can be marred by poor fabrication, usually no good fabrication can disguise poor design.

### Models of the Design Process

- Create a solution.
- Build a model of the solution.
- Test the model against the original requirements.
- Elaborate the model to produce a specification for the solution.

## Design

- Design methods and patterns: help determine which choice is the best for a given situation.
- Representations: help with the process of building models of the intended system and with evaluating its behaviour.
- Abstraction: is concerned with the removal of detail from a description of a problem, while still retaining the essential properties of its structure; it is essential to build manageable models of large and complex systems.

### Design Principles

Fundamental guidelines that inform good software design decisions.

#### SOLID Principles

**S - Single Responsibility Principle (SRP)**

- A class should have only one reason to change.
- Each class should have only one responsibility or job.
- Promotes high cohesion and low coupling.
- Makes code easier to understand, test, and maintain.

**O - Open/Closed Principle (OCP)**

- Software entities should be open for extension but closed for modification.
- Can add new functionality without changing existing code.
- Achieved through abstraction, inheritance, and polymorphism.
- Reduces risk of breaking existing functionality.

**L - Liskov Substitution Principle (LSP)**

- Objects of a superclass should be replaceable with objects of a subclass without breaking the application.
- Subtypes must be substitutable for their base types.
- Ensures that inheritance is used correctly.
- Preserves behavioral compatibility.

**I - Interface Segregation Principle (ISP)**

- Clients should not be forced to depend on interfaces they don't use.
- Many specific interfaces are better than one general-purpose interface.
- Prevents "fat" interfaces with unrelated methods.
- Reduces coupling and improves flexibility.

**D - Dependency Inversion Principle (DIP)**

- High-level modules should not depend on low-level modules; both should depend on abstractions.
- Abstractions should not depend on details; details should depend on abstractions.
- Promotes decoupling and testability.
- Enables flexibility and easier replacement of components.

#### Other Key Principles

**DRY - Don't Repeat Yourself**

- Every piece of knowledge should have a single, unambiguous representation.
- Avoid code duplication.
- Changes should require modification in only one place.
- Improves maintainability and reduces errors.

**KISS - Keep It Simple, Stupid**

- Systems work best when kept simple rather than made complex.
- Avoid unnecessary complexity.
- Simple solutions are easier to understand, maintain, and debug.
- Complexity should only be added when necessary.

**YAGNI - You Aren't Gonna Need It**

- Don't add functionality until it's actually needed.
- Avoid speculative development.
- Reduces code bloat and maintenance burden.
- Focus on current requirements.

**Separation of Concerns**

- Different aspects of a system should be separated into distinct sections.
- Each section addresses a specific concern.
- Reduces coupling between different parts of the system.
- Makes systems more modular and maintainable.

**Information Hiding**

- Implementation details should be hidden behind well-defined interfaces.
- Users of a module need only know the interface, not the implementation.
- Enables changes to implementation without affecting clients.
- Fundamental to encapsulation.

**Coupling and Cohesion**

_Coupling_: Degree of interdependence between modules.

- Low coupling is desirable.
- Types (from best to worst): data coupling, stamp coupling, control coupling, common coupling, content coupling.
- Low coupling improves reusability, maintainability, and testability.

_Cohesion_: Degree to which elements within a module belong together.

- High cohesion is desirable.
- Types (from best to worst): functional, sequential, communicational, procedural, temporal, logical, coincidental.
- High cohesion means each module has a well-defined purpose.

**Goal**: Aim for low coupling and high cohesion.

### Viewpoints

The designer will usually make use of a number of different forms of design representation.
Each representation provides a different viewpoint on the form of a design.

'Wicked' problems: a problem whose form is such that a solution for one of its aspects simply changes the problem

## Architectural Styles

### Module-centered styles

#### Layered

Context: structure systems that are organized into a number of layers, each of which provides services to the layer above it and uses services from the layer below it.

Types of elements:

- Layers: a collection of related functionality that is organized into a single unit. Its interface provides services to the layer above it and uses services from the layer below it.

Types of relationships:

- "allowed-to-use" relationship: any element in a layer can use the public services of the layer below it.

Constraints:

- Each layer can only use services from the layer directly below it.
- Atleast 2 layers.
- All elementary code units belong to exactly 1 layer.
-

Properties:

- modifiability: cohesion of the set services provided by each layer.
- portability: dependencies are local, changes at one level can only affect adjacent levels.
- testability: each layer can be tested independently.
- reusability and evolution: layers can be replaced by new implementations as long as the interface remains the same.
- not always easy or possible to structure a system in layers.
- difficult to estabilish granularity of layers.
- may incur performance penalties.

### Data-flow styles

Determined by the flow of data through the system. Applies when data availability controls computation and the flow pattern is explicit and is the only way components communicate.

Properties:

- components are highly independent.
- no global control of the components behaviour.
- processing elements can be executed concurrently.
- continuous control and monitoring functions of real-time.
- reusable.

Modification can be done at the component level or the structural level.
Data flow arch can be analysed for its performance.
A possible difficulty is the synchronization of computations.

#### Batch sequential

Context: sequential data processing systems where data is processed in discrete batches.

Types of elements:

- Data Transformer: transforms input data into output data, limited to input and output data ports.

Types of connectors:

- Data Flow: direct the result of a data transformer to the input of another data transformer.

Computational model:

- Data transformers execute sequentially.
- Consists of a finite number of steps linearly connected.

Advantages:

- almost all of the data flow architectural style especially the reusability and modifiability.
- several executions, simplicty, easy to understand.
- avoids complicated issues related to synchronization and concurrency via sequential execution.

Disadvantages:

- not very fault-tolerant.
- parallelism is limited.
- not suitable for continuous flows of data of undefined length.

#### Pipe and filter

Context: sequential and incremental processing of a stream of data.

Proposal: structure around filters that encapsulate each processing step and are independent of each other, specifically not sharing state information or knowing the identity of the filters that feed them or the filters they feed.

Possible specializations:

- Pipelines: restrict the topology to be a linear sequence of filters.
- Pipes with limited capacity: restrict the amount of data that can be in a pipe.
- Pipes with Types: restricts the type of data that can flow through a pipe.

Types of elements:

- Filter: a processing element that transforms input data into output data. It has input and output data ports. Independent of other filters.

Types of connectors:

- Pipe: directs the output data of one filter to the input data port of another filter.

Computational model:

- All elements execute until there is no more data to process.

Advantages:

- simple.
- reusable and flexible.
- performant due to potential for parallelism (throughput).
- data incrementally processed (latency).

Disadvantages:

- data to be exchanged should be simply.
- no interaction between components.
- not good at interactive systems.
- extra performance overhead due to data conversion and communication through pipes.

### Repository styles

Data-centered styles where the flow of data is determined by access to shared data. Components interact only through a shared data store.

Properties:

- centralized data management.
- components are independent of each other.
- components communicate only through the repository.
- good for data-intensive applications.

#### Shared-data

Context: systems where multiple components need access to shared data and data integrity is important.

Proposal: organize components around a central data repository that all components can access.

Types of elements:

- Central data store: repository that stores and manages data.
- Data accessor: components that read from and write to the central data store.

Types of connectors:

- Data access: mechanisms for reading and writing to the central data store.

Computational model:

- Components are independent and communicate only through the data store.
- Control is determined by the data accessors, not the repository.

Advantages:

- data consistency and integrity.
- centralized backup and security.
- components are independent and can be developed separately.
- efficient data sharing.
- scalability through data store optimization.

Disadvantages:

- central data store can become a bottleneck.
- single point of failure.
- tight coupling between components and data schema.
- difficult to distribute.

#### Blackboard

Context: complex problems that require collaboration of diverse specialized subsystems and no deterministic solution strategy exists.

Proposal: collection of independent components that cooperate to find a solution by updating a shared data structure (blackboard), controlled by a control component.

Types of elements:

- Blackboard: shared data structure that holds the current state of the problem and partial solutions.
- Knowledge sources: independent components that provide specialized problem-solving capabilities.
- Control: manages the execution of knowledge sources based on the blackboard state.

Types of connectors:

- Data access: reading and writing to the blackboard.

Computational model:

- Knowledge sources monitor the blackboard for changes.
- When a knowledge source can contribute, it updates the blackboard.
- Control component decides which knowledge source to activate next.
- Process continues until a solution is found or no progress can be made.

Advantages:

- flexibility in combining different problem-solving approaches.
- opportunistic problem solving.
- reusable knowledge sources.
- supports experimentation with different strategies.
- fault tolerance through redundancy.

Disadvantages:

- complex to design and implement.
- difficult to debug and test.
- no guaranteed solution or termination.
- synchronization and concurrency issues.
- performance can be unpredictable.

### Event-based styles

Components communicate through events. Decouples event producers from event consumers.

Properties:

- loose coupling between components.
- asynchronous communication.
- scalability and flexibility.
- dynamic system reconfiguration.

#### Publish-Subscribe (Pub-Sub)

Context: systems where components need to react to changes in state or events without tight coupling.

Proposal: components can publish events and subscribe to events of interest without knowing about each other.

Types of elements:

- Publisher: components that generate and publish events.
- Subscriber: components that subscribe to and process events.
- Event bus/broker: mediates event distribution from publishers to subscribers.

Types of connectors:

- Event publication: publishing events to the event bus.
- Event subscription: subscribing to specific event types.
- Event notification: delivering events from bus to subscribers.

Computational model:

- Publishers emit events to the event bus without knowing subscribers.
- Event bus delivers events to all interested subscribers.
- Subscribers process events asynchronously.
- Execution is event-driven.

Advantages:

- loose coupling between components.
- dynamic system evolution (add/remove publishers and subscribers).
- scalability through parallel event processing.
- supports distributed systems.
- flexibility and reusability.

Disadvantages:

- difficult to understand system behavior and data flow.
- testing and debugging complexity.
- no guaranteed delivery or ordering (without additional mechanisms).
- potential for event storms.
- complexity in error handling and recovery.

### Call-return styles

Based on procedure calls and returns. Hierarchical organization with explicit invocation.

Properties:

- explicit invocation.
- synchronous communication.
- well-defined interfaces.
- hierarchical control flow.

#### Client-Server

Context: systems where functionality is divided between service providers (servers) and service requesters (clients).

Proposal: separate the system into clients that request services and servers that provide services.

Types of elements:

- Client: initiates requests for services.
- Server: provides services and responds to requests.

Types of connectors:

- Request/reply: synchronous or asynchronous communication protocol.

Computational model:

- Client sends request to server.
- Server processes request and sends response.
- Client waits for response (synchronous) or continues (asynchronous).

Advantages:

- centralized control and data management.
- easier maintenance of servers.
- scalability through multiple clients.
- clear separation of concerns.
- security can be centralized.

Disadvantages:

- server can be a bottleneck.
- single point of failure.
- network dependency.
- limited scalability of server.

#### Peer-to-Peer (P2P)

Context: distributed systems where all nodes have equal capabilities and responsibilities.

Proposal: eliminate distinction between client and server; each node can act as both.

Types of elements:

- Peer: a component that can both request and provide services.

Types of connectors:

- Bidirectional communication: peers communicate directly with each other.

Computational model:

- Peers discover each other through various mechanisms.
- Any peer can initiate requests to other peers.
- Any peer can respond to requests from other peers.
- Decentralized control and data.

Advantages:

- no single point of failure.
- scalability through distributed resources.
- fault tolerance through redundancy.
- resource sharing efficiency.
- self-organizing.

Disadvantages:

- complex to implement and manage.
- security and trust issues.
- difficult to maintain data consistency.
- variable quality of service.
- discovery and coordination complexity.

#### Broker

Context: distributed systems with complex service interactions where clients need to discover and access services without tight coupling.

Proposal: introduce a broker component that mediates communication between clients and servers.

Types of elements:

- Client: requests services through the broker.
- Server: registers services with the broker and provides them.
- Broker: mediates between clients and servers, handles service discovery and routing.

Types of connectors:

- Client-broker: client requests services.
- Broker-server: broker forwards requests and returns responses.
- Server registration: servers register their services with broker.

Computational model:

- Servers register their services with the broker.
- Clients request services from the broker.
- Broker locates appropriate server and forwards request.
- Server processes request and returns response through broker.
- Broker returns response to client.

Advantages:

- location transparency: clients don't need to know server locations.
- loose coupling between clients and servers.
- dynamic service discovery.
- easier to add new services.
- centralized security and monitoring.
- load balancing possibilities.

Disadvantages:

- broker can be a bottleneck.
- broker is a single point of failure (without redundancy).
- added latency due to indirection.
- increased complexity.
- broker must be highly reliable.

#### Service-Oriented Architecture (SOA)

Context: enterprise systems that need to integrate heterogeneous applications and services across organizational boundaries.

Proposal: organize functionality as interoperable services with well-defined interfaces, typically using web service standards.

Types of elements:

- Service provider: implements and offers services.
- Service consumer: uses services.
- Service registry: directory of available services.
- Service bus (ESB): mediates communication between services.

Types of connectors:

- Service invocation: typically SOAP, REST, or messaging protocols.
- Service discovery: querying the service registry.

Computational model:

- Service providers register services in the registry.
- Service consumers discover services through the registry.
- Consumers invoke services using standard protocols.
- Enterprise Service Bus (ESB) may mediate complex interactions.

Advantages:

- interoperability across platforms and languages.
- reusability of services.
- loose coupling.
- business-IT alignment through service abstraction.
- easier integration of legacy systems.
- supports distributed development.

Disadvantages:

- complexity and overhead (especially with ESB).
- performance overhead due to XML/SOAP processing.
- governance challenges.
- can become overly complex.
- service versioning difficulties.
- testing complexity.

#### Microservices

Context: complex applications that need to be highly scalable, maintainable, and deployable independently.

Proposal: decompose the application into small, independent services that communicate over lightweight protocols, each owning its data.

Types of elements:

- Microservice: small, autonomous service focused on a single business capability.
- API Gateway: optional entry point that routes requests to appropriate microservices.
- Service registry: tracks available service instances.

Types of connectors:

- Lightweight protocols: typically REST/HTTP, gRPC, or message queues.
- API composition: aggregating data from multiple services.

Computational model:

- Each microservice runs independently.
- Services communicate through well-defined APIs.
- Each service manages its own database.
- Services are deployed, scaled, and updated independently.
- Discovery mechanisms help services find each other.

Advantages:

- independent deployment and scaling.
- technology diversity (polyglot architecture).
- fault isolation: failure in one service doesn't crash others.
- easier to understand and modify individual services.
- enables continuous delivery and deployment.
- team autonomy and parallel development.
- resilience through redundancy.

Disadvantages:

- distributed system complexity.
- network latency and reliability issues.
- data consistency challenges (eventual consistency).
- testing complexity (integration and end-to-end).
- operational complexity (monitoring, logging, tracing).
- service coordination overhead.
- difficult to refactor across service boundaries.

### Ad-hoc reuse Techniques

#### Furtuitous and small-scale

Reuse libraries with algorithms/modules/structures/components that are developed in different projects and encourage the use of these in new projects.

Takes longer to locate and integrate them than to build from scratch.

#### Clone and own

Developing a new project similar to one built before, modifying where necessary, adding whats missing, turning it into a product. Separate maintenance path. MariaDB fork of MySQL is an example, or Jenkins from Hudson.

Pros and cons:

- fast and cheap (at first).
- costs in terms of maintaining the various copies quickly become very high.
- costs of having inconsistent copy evolution.

## Quality Attributes

Quality attributes (also called non-functional requirements) are measurable properties of a system that indicate how well the system satisfies stakeholder needs beyond its basic functionality.

### Categories of Quality Attributes

#### Runtime Quality Attributes

Observable during system execution:

**Performance**

- Response time, throughput, latency.
- How quickly the system responds to events.
- Resource utilization (CPU, memory, bandwidth).

**Security**

- Ability to protect data and resources.
- Authentication, authorization, encryption.
- Resistance to attacks.
- Data integrity and confidentiality.

**Availability**

- Proportion of time the system is operational.
- Mean Time Between Failures (MTBF).
- Mean Time To Repair (MTTR).
- Fault tolerance and resilience.

**Usability**

- Ease of use for end users.
- Learning curve.
- User satisfaction.
- Accessibility.

**Reliability**

- Ability to perform required functions under stated conditions.
- Consistency of behavior.
- Probability of failure-free operation.

**Scalability**

- Ability to handle growing amounts of work.
- Horizontal (add more machines) vs vertical (add more power).
- Performance under increasing load.

#### Development-time Quality Attributes

Observable during development and maintenance:

**Modifiability**

- Ease of making changes to the system.
- Cost and risk of making changes.
- Includes maintainability and extensibility.

**Testability**

- Ease of demonstrating faults through testing.
- Controllability and observability.
- Test coverage capabilities.

**Portability**

- Ease of moving the system to different environments.
- Platform independence.
- Adaptability to different contexts.

**Reusability**

- Extent to which assets can be used in other systems.
- Reduces development time and cost.

**Integrability**

- Ease of integrating the system with other systems.
- Interoperability with external components.

### Quality Attribute Tradeoffs

Quality attributes often conflict with each other:

- **Performance vs Security**: Encryption adds overhead.
- **Performance vs Modifiability**: Optimizations can make code harder to change.
- **Security vs Usability**: Strong authentication can be cumbersome.
- **Availability vs Cost**: Redundancy is expensive.
- **Time-to-market vs Quality**: Rushing can compromise quality.

Architectural decisions must balance these competing concerns based on stakeholder priorities.

## Quality Attribute Scenarios

A structured, precise method for specifying quality attribute requirements using a 6-part scenario.

### The 6-Step Scenario Structure

**1. Source of Stimulus**

- Who or what generates the stimulus.
- Can be human, computer system, or other actor.
- Example: End user, external system, attacker, developer.

**2. Stimulus**

- The condition or event that triggers the scenario.
- What happens to cause the system to respond.
- Example: User request, component failure, code change request, attack attempt.

**3. Environment**

- The context or conditions under which the stimulus occurs.
- System state when stimulus arrives.
- Example: Normal operation, overload, startup, maintenance mode.

**4. Artifact**

- The part of the system affected by the stimulus.
- What receives the stimulus.
- Example: Entire system, specific subsystem, process, database.

**5. Response**

- The activity undertaken as a result of the stimulus.
- How the system should react.
- Example: Process request, log failure, isolate fault, reject access.

**6. Response Measure**

- Quantifiable measure to test whether the response is adequate.
- How success is measured.
- Example: Response time < 2 seconds, 99.9% uptime, detect attack in < 1 minute.

### Example Scenarios

**Performance Scenario:**

1. Source: End user
2. Stimulus: Initiates a transaction
3. Environment: Normal operations, moderate load
4. Artifact: System
5. Response: Processes transaction and returns result
6. Response Measure: Within 2 seconds for 95% of requests

**Modifiability Scenario:**

1. Source: Developer
2. Stimulus: Wishes to change the database schema
3. Environment: Design time
4. Artifact: Database access layer
5. Response: Changes are made, tested, and deployed
6. Response Measure: Within 8 hours of work, affecting no more than 5 modules

**Availability Scenario:**

1. Source: Hardware failure
2. Stimulus: Server crashes
3. Environment: Normal operation
4. Artifact: Web server
5. Response: System detects failure, switches to backup server, logs incident
6. Response Measure: Service restored within 30 seconds, zero transactions lost

**Security Scenario:**

1. Source: Unauthorized user
2. Stimulus: Attempts to access sensitive data
3. Environment: System under normal operation
4. Artifact: Authentication system
5. Response: Denies access, logs attempt, alerts administrator
6. Response Measure: Access denied within 1 second, alert sent within 5 seconds

### Benefits of Quality Attribute Scenarios

- Provides precise, testable requirements.
- Forces stakeholders to be specific about their needs.
- Enables early detection of conflicting requirements.
- Facilitates architectural evaluation.
- Serves as basis for acceptance testing.
- Improves communication between stakeholders and architects.

## Architectural Styles vs Architectural Patterns

Architectural styles are general patterns that can be applied to a wide range of systems, while architectural patterns are more specific solutions tailored to particular problems within a given context.

### Structural vs Functional decomposition

Structural decomposition focuses on breaking down a system into its physical components or modules, emphasizing the organization and relationships between these components. Functional decomposition, on the other hand, breaks down a system based on its functions or processes, focusing on the tasks that need to be performed and how they interact to achieve the overall system goals.

A reference model is a division of functionality together with data flow between the pieces, standard decomposition of a known problem into parts that cooperatively solve the problem.

A reference architecture is a more concrete architecture that implements a reference model onto software elements, providing a template solution for a specific domain or problem.

## Views and view types

Group sets of design decisions related by common concerns.

Types of views:

- **Logical view**: Focuses on the functionality that the system provides to end-users. Shows the key abstractions (classes, objects, etc.) and their relationships.
- **Development (or Implementation) view**: Describes the static organization of the software in its development environment (modules, components, packages).
- **Process view**: Addresses the dynamic aspects, explaining the system processes and how they communicate, focusing on concurrency and synchronization.
- **Physical (Deployment) view**: Shows how the system is mapped onto the hardware and how components are distributed across nodes.
- **Scenarios (Use case view)**: Illustrates how the elements in the other views work together to realize a set of use cases or scenarios.

**Example:**

Suppose we are designing an online bookstore:

- _Logical view_: Classes like `Book`, `ShoppingCart`, `User`, and their relationships.
- _Development view_: Code is organized into packages such as `catalog`, `order`, `payment`.
- _Process view_: Separate processes for web server, payment processing, and inventory management.
- _Physical view_: Web server and database server run on different machines; load balancer distributes requests.
- _Scenarios_: A user searches for a book, adds it to the cart, and completes a purchase.

### Software Product Lines (SPL)

Based on a well-knwn concept in manufacturing industry.
In the context of a software product line approach, reuse is planned and mechanisms are placed to ensure reuse is possible, occurs and is profitable.

A software product line is a set of software-intensive systems that share a common, managed set of features satisfying the specific needs of a particular market segment or mission and that are developed from a common set of core assets in a prescribed way.

Software product lines are a software development paradigm allowing companies to realize order-of-magnitude improvements in time to market, cost, productivity, quality, and other business drivers.

#### Feature Modeling

A feature model is a compact representation of all the products of the software product line in terms of "features" (prominent or distinctive user-visible aspects, qualities, or characteristics of a software system).

#### Variability

Variability is the ability of a software system or artifact to be efficiently extended, changed, customized, or configured for use in a particular context.

# DS

## Software Development

### Software Development Life Cycle (SDLC)

Planning -> Design -> Coding -> Testing -> Deployment -> Maintenance -> ...

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

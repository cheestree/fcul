# Design de Software

## Worksheet 4

### 1 - Explanation of bridge between problem space and solution space

#### a. Applied to tax assessment software

The software is modeled so that it can meet the end users' necessity and throughput, while maintaining a low-cost model for the state. This tends to make or break it depending on the usability, specifically what happens most years where, due to a lot of users accessing the website and making requests, crashes the servers, making it unusable for some time.

#### b. Applied to augmented reality translation software

The most popular languages are prioritized due to a higher usage and, so, users. This means that the software is available for the majority of the userbase, garnering more funding and also more time for developers to incrementally add new languages.

### 2 - Structures of software architecture

The repository layer and how it connects and queries databases, the service layer where actual operations are executed based on input data, or the web layer, where the server receives the users' requests and processes it before sending it to the service layer.  
All of these 3 layers are in need of doccumentation due to the ever changing software needs.

### 3 - Decomposition structure

#### a. Type of elements and relationships of Decomposition

It describes modules and a "is-part-of" relation, like encapsulation.

#### b. Data and control flow of Decomposition

No loops are allowed, so one can't be part of another that is already a part of itself. It will always answer to the higher-up module.

#### c. Usefulness of Decomposition

To assign responsibilities to modules as prelude to downstream work. It also helps in conducting impact analysis, developing work assignments and communicating to new developers, in chunks, how the software is organized.

### 4 - Allowed-to-use structure

#### a. Type of elements and relationships of ALlowed-to-use

It describes layers and the usage definition rules. A layer is allowed to use any lower layer, or only the layer directly under it.

#### b. Usefulness of Allowed-to-use

It promotes portability and modifiability, incremental development, separation of concerns and reuse.

#### c. Comparison of Allowed-to-use and Decomposition

One is better for a overview analysis, while the other is a more strict, rule-based architecture for interactions between modules.

### 5 - Aggregated modules, or subsystems

#### a. Subsystems of a Mars exploratory robot

Several subsystems that might compose a Mars exploratory robot include:

1. **Navigation and Mobility Subsystem**
   - Path planning algorithms
   - Obstacle avoidance
   - Wheel/track control systems
   - Positioning and mapping (SLAM)

2. **Power Management Subsystem**
   - Solar panel control
   - Battery management
   - Power distribution
   - Energy optimization

3. **Communication Subsystem**
   - Data transmission to Earth
   - Signal processing
   - Antenna control
   - Protocol management

4. **Scientific Instrumentation Subsystem**
   - Camera systems
   - Spectrometers
   - Drilling equipment
   - Sample collection and analysis

5. **Environmental Monitoring Subsystem**
   - Weather station
   - Radiation monitoring
   - Temperature sensors
   - Atmospheric analysis

6. **Mission Control and Planning Subsystem**
   - Command interpretation
   - Task scheduling
   - Mission objectives management
   - Autonomous decision making

#### b. Math utility library as a subsystem

No, a math utility library would **not** be considered a subsystem of the exploratory robot system.

**Justification:**

- A subsystem should carry out a functionally cohesive subset of the overall system's mission
- A math library is a **supporting utility** that provides computational services to other subsystems
- It doesn't directly contribute to the robot's exploration mission but rather enables other subsystems to perform calculations
- It's more appropriately classified as a **shared module** or **utility layer** that multiple subsystems depend on
- Unlike true subsystems, it cannot be executed independently in the context of the robot's mission

#### c. Layered design for Mars exploratory robot system

```text
┌─────────────────────────────────────────────────────────────┐
│                    Mission Control Layer                    │
│          (High-level planning, goal management)             │
├─────────────────────────────────────────────────────────────┤
│                 Subsystem Coordination Layer                │
│        (Inter-subsystem communication, scheduling)          │
├─────────────────────────────────────────────────────────────┤
│  Navigation  │ Scientific │ Communication │ Environmental  │
│   & Mobility │Instruments │               │  Monitoring    │
│   Subsystem  │ Subsystem  │   Subsystem   │   Subsystem    │
├─────────────────────────────────────────────────────────────┤
│                    Service/Utility Layer                    │
│  (Math libraries, data structures, common algorithms)       │
├─────────────────────────────────────────────────────────────┤
│                    Hardware Abstraction Layer               │
│        (Device drivers, sensor interfaces, actuators)       │
├─────────────────────────────────────────────────────────────┤
│                       Hardware Layer                        │
│    (Processors, sensors, actuators, communication hardware) │
└─────────────────────────────────────────────────────────────┘
```

#### d. Are subsystems a partition of the system?

No, the subsystems are **not** considered to be a partition of the system in separate parts.

- In a true partition, each element belongs to exactly one subset with no overlap
- Subsystems in complex systems like a Mars robot often **share resources** and have **overlapping responsibilities**
- For example:
  - The Power Management subsystem interacts with ALL other subsystems
  - The Communication subsystem may share processors with Navigation
  - Environmental data collected by the Environmental Monitoring subsystem is used by Navigation for decision-making
- Subsystems are better understood as **overlapping functional domains** rather than mutually exclusive partitions
- They represent different **concerns** or **responsibilities** that may share underlying resources and components
- The system architecture allows for **cross-cutting concerns** where certain functionalities (like logging, error handling, or power management) span multiple subsystems

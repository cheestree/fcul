# Software Security Notes

## Basic Concepts

Confidentiality, Integrity and Availability.

**0-day Vulnerability**: unknown to those who would be interested in mitigating it, including the vendor of the target software.
**Design** vulnerability: the result of a fundamental design flaw in a system or application.
**Coding** vulnerability: arises from errors or oversights in the code of a system or application.
**Operational** vulnerability: results from weaknesses in the operational procedures or configurations of a system.

**Attack**: An attempt to exploit a vulnerability in order to compromise the confidentiality, integrity, or availability of a system or its data.
**Exploit**: A specific method or technique used to take advantage of a vulnerability in order to carry out an attack.
**Patch**: A software update that addresses vulnerabilities or bugs in a system or application.

**Attack Vector**: The path or means by which an attacker gains access to a system or network in order to carry out an attack.

**Attack Surface**: The total sum of all the points (attack vectors) where an unauthorized user can try to enter or extract data from a system. User interface, network services, file systems, APIs, etc. are all part of the attack surface. Then operating system, and only after the application.

## SDLC

**Waterfall** model: A linear and sequential approach to software development where each phase must be completed before the next phase begins. It is characterized by distinct phases such as requirements gathering, analysis, design, implementation, testing, deployment, and maintenance.
**Design** vulnerabilities are often discovered late in the process, making them costly to fix, while **coding** vulnerabilities may be easier to address during the implementation phase. **Operational** vulnerabilities may not be fully addressed until the maintenance phase, when real-world usage reveals weaknesses in procedures or configurations.

**Open-source vs closed-source**: Open-source software allows anyone to view, modify, and distribute the source code, which can lead to more eyes on the code and potentially quicker identification and resolution of vulnerabilities (can be viewed by all, malicious or not). Closed-source software restricts access to the source code, which can limit the number of people who can identify vulnerabilities but may also reduce the risk of attackers exploiting known vulnerabilities (security by obscurity is not a good idea).

**Never** assume trust of input, **always** validate and sanitize.
**Always** use authentication mechanisms that can't be bypassed (authorization **AFTER** authentication).
**Identify** and **protect** sensitive data.
Understand external components.
Preparation for system evolution and maintenance.

Keep security mechanisms **as simple as possible**.
Fail-safe defaults (based on giving permission instead of defining exclusion, ie default is no access).
**Every** access must be checked for **authority**.
**Open design** (security should not depend on secrecy of design or implementation).
**Separation of privilege** (multiple layers of security).
**Least** privilege (give only the minimum access necessary).
**Least** common mechanism (minimize the amount of mechanism common to more than one user and depended on by all users).
**Psychological acceptability** (security mechanisms should not make the resource more difficult to access than if the security mechanisms were not present).

## Dangerous APIs

### Memory Organization

**Stack**: used for function call management, including local variables, function parameters, and return addresses. It operates in a last-in, first-out (**LIFO**) manner.
**Heap**: used for dynamic memory allocation. It grows and shrinks as memory is allocated and deallocated during program execution.
**BSS**: uninitialized global and static variables. It is typically allocated at program startup and is zero-initialized by the operating system.
**Data**: initialized global and static variables. It is typically divided into read-only and read-write sections.
**Text**: the executable code of a program. It is typically read-only to prevent accidental modification of instructions during execution.

### Common Vulnerabilities

**Buffer** Overflow: A vulnerability that occurs when a program writes more data to a buffer than it can hold, potentially overwriting adjacent memory and leading to crashes or arbitrary code execution. Usually occurs via unsafe functions like strcpy, strcat, gets, scanf without length checks. Can be exploited to overwrite return addresses on the stack (stack-based buffer overflow) or function pointers in the heap (heap-based buffer overflow), may or may not lead to correct program execution.

**Heap** Overflow: A type of buffer overflow that occurs when a program writes more data to a heap-allocated buffer than it can hold, potentially overwriting adjacent memory and leading to crashes or arbitrary code execution. Can be exploited to overwrite function pointers or other control structures in the heap, may or may not lead to correct program execution.

**Stack** Overflow: A type of buffer overflow that occurs when a program writes more data to a stack-allocated buffer than it can hold, potentially overwriting adjacent memory and leading to crashes or arbitrary code execution. Can be exploited to overwrite return addresses on the stack, may or may not lead to correct program execution.

**Never** trust user input, **always** validate and sanitize. **Never** assume anything about someone else's code.

### Solutions

**ASLR** (**Address Space Layout Randomization**): A security technique that **randomizes** the **memory addresses** used by a program, making it more difficult for attackers to predict the location of specific functions or data structures. This helps to mitigate buffer overflow attacks by making it harder for attackers to exploit known memory addresses.
**DEP** (**Data Execution Prevention**): A security feature that marks certain areas of **memory** as **non-executable**, preventing code from being executed in those regions. This helps to mitigate buffer overflow attacks by preventing injected code from being executed.
**Canary** Values: A security mechanism that **places a small, known value (the "canary")** before the return address on the stack. If a buffer overflow occurs and overwrites the return address, the canary value will **also** be modified. Before returning from a function, the program checks the canary value; if it has changed, the program can take appropriate action (e.g., terminate the program) to prevent exploitation.
**Safe** Libraries: Using safer alternatives to unsafe functions
**Control Flow Integrity**: A security technique that ensures that the control flow of a program follows a predetermined path, preventing attackers from redirecting execution to malicious code. This can be achieved through techniques such as function pointer validation, return address verification, and indirect branch tracking.

### Advanced Overflows

**Return-to-libc** Attack: An attack that exploits a buffer overflow vulnerability to redirect the program's control flow to existing functions in the C standard library (libc), such as system() or execve(). By overwriting the return address on the stack with the address of a libc function, an attacker can execute arbitrary commands without injecting new code into the program.
**Return-Oriented Programming** (ROP): An advanced exploitation technique that involves **chaining together small snippets of existing code** (called "gadgets") that end with a **return** instruction. By carefully crafting the stack to contain the addresses of these gadgets, an attacker can **execute arbitrary code** without injecting new code into the program. **ROP** is often used to bypass security mechanisms such as **DEP** and **ASLR**.
**Heap Spray**: A technique used by attackers to increase the likelihood of successful exploitation of memory corruption vulnerabilities, such as buffer overflows. The attacker fills the heap with a large amount of malicious data (often shellcode) in the hope that when a vulnerability is triggered, the program will execute the attacker's code. This technique is often used in conjunction with other exploitation methods, such as ROP or return-to-libc attacks.
**Modify a pointer**: An attacker exploits a vulnerability to change the value of a pointer variable, redirecting it to point to malicious data or code. This can lead to unauthorized access, data corruption, or arbitrary code execution when the program dereferences the modified pointer. Difficult if canary values or safe libraries are used.
**Function-pointer clobbering**: An attacker exploits a vulnerability to overwrite a function pointer variable with the address of malicious code. When the program later calls the function through the overwritten pointer, it executes the attacker's code instead of the intended function. Difficult if control flow integrity mechanisms are in place.
**Data-pointer modification**: An attacker exploits a vulnerability to change the value of a data pointer variable, redirecting it to point to sensitive data or code. This can lead to unauthorized access, data corruption, or arbitrary code execution when the program dereferences the modified pointer. Difficult if memory protection mechanisms are in place.
**Hijacking Exception Handlers**: An attacker exploits a vulnerability to overwrite the address of an exception handler with the address of malicious code. When an exception occurs, the program executes the attacker's code instead of the intended handler. Difficult if control flow integrity mechanisms are in place.
**Virtual Pointer Overflow**: An attacker exploits a vulnerability to overwrite a virtual function pointer in an object-oriented program. When the program calls the virtual function, it executes the attacker's code instead of the intended function. Difficult if control flow integrity mechanisms are in place.
**Use-After-Free**: An attacker exploits a vulnerability that allows them to access memory that has already been freed. By manipulating the program's memory allocation and deallocation, the attacker can gain access to sensitive data or execute arbitrary code. Difficult if safe memory management practices are followed.
**Off-by-One**: An attacker exploits a vulnerability that allows them to write one byte beyond the bounds of a buffer. This can lead to memory corruption, data leakage, or arbitrary code execution. Difficult if safe libraries and bounds checking are used.

### Upcasting and Downcasting

**Upcasting** (cast from a derived class to its parent class) is ***always safe***, **downcasting** (from a parent class to one of its derived classes) is **not**. Properties of the derived class **may not** exist in the parent class, leading to **undefined behavior**, like accessing areas of memory with sensitive data. Use **dynamic_cast** for downcasting to ensure **safety** at runtime.

### Integer Overflow

**Overflow**: occurs when an arithmetic operation produces a result that exceeds the maximum value that can be stored in a given data type. This can lead to unexpected behavior, such as wrapping around to a negative value or zero.
**Underflow**: occurs when an arithmetic operation produces a result that is smaller than the minimum value that can be stored in a given data type. This can also lead to unexpected behavior, such as wrapping around to a large positive value.
**Signedness error**: occurs when a signed integer is mistakenly treated as an unsigned integer, or vice versa. This can lead to unexpected behavior, such as negative values being interpreted as large positive values due to the way signed and unsigned integers are represented in binary (most important bit represents the sign).
**Trucantion**: occurs when a value is converted from a larger data type to a smaller data type, resulting in the loss of some of the original value's bits. This can lead to unexpected behavior, such as data corruption or incorrect calculations.

## Protection of Resources

### Separation

When software tries executing operations in objects outside its control, it calls the **OS kernel** via **system** calls. The kernel runs in a more privileged mode (**supervisor** mode) than user applications (**user** mode). The CPU switches between these modes using a hardware mechanism called a **mode bit**. Uses software interruption to switch from user mode to kernel mode.

Types of separation:

- **Physical**: different processes use **distinct** devices.
- **Temporal**: different processes use the **same** device at different times.
- **Logical**: different processes share the **same** device but **cannot** interfere with each other/no other processes exist for them (most common).
- **Cryptographic**: data is **encrypted** so that only **authorized** processes can access it.

#### Solution

**Segmentation**: Divides memory into **different segments** based on the **type** of data (code, data, stack, heap). Each **segment** has its **own access permissions**, preventing unauthorized access to sensitive areas of memory. Uses a **translation table** to map logical addresses to physical addresses. Keeps track of different segments and their permissions. Difficult to efficiently check if memory accesses are within segment limits, can cause fragmentation.

**Paging**: Divides memory into **fixed-size pages** (typically 4KB). Each page can be mapped to any physical memory location, allowing for more efficient use of memory and easier management of memory allocation. Uses a **page table** to map logical addresses to physical addresses. Simplifies memory management and reduces fragmentation, but can introduce overhead due to page table lookups. Process can only access its **own pages**, preventing unauthorized access to other processes' memory.

**Segmentation+Paging**: Combines both segmentation and paging to provide a more **flexible and efficient** memory management system. Memory is **divided** into **segments**, which are further divided into **pages**. Each segment has its **own page table**, allowing for **fine-grained control** over memory access and allocation. Provides the benefits of both segmentation and paging, but can introduce additional complexity in managing segment and page tables.

### Mediation through Access Control

Concerned about who can access what resources and under what conditions.

Basic models:

- **ACL** (**Access Control List**): A list associated with each resource that specifies which users or groups have access to the resource and what actions they can perform (read, write, execute).
- **Capability**: A token or key that grants a user or process the right to access a resource. Capabilities can be passed between processes, allowing for more flexible access control.
- **ACM** (**Access Control Matrix**): A matrix that defines the access rights of each user or process for each resource in the system. Rows represent users/processes, columns represent resources, and the entries specify the access rights.

### Applying to Systems

**DEP** (Data Execution Prevention): A security feature that marks certain areas of memory as non-executable, preventing code from being executed in those regions. This helps to mitigate buffer overflow attacks by preventing injected code from being executed.
**ASLR** (Address Space Layout Randomization): A security technique that randomizes the memory addresses used by a program, making it more difficult for attackers to predict the location of specific functions or data structures. This helps to mitigate buffer overflow attacks by making it harder for attackers to exploit known memory addresses.

## Input Validation

Something can be **trusted** without being **trustworthy**. **Never** trust user input.
Attack surface can range from a socket or a webservice, to an API, files used by the application, or even the user interface and operating system.

### Vulnerabilities

**Format String Vulnerability**: Occurs when user input is used as a format string in functions like printf **without** proper validation. An attacker can exploit this vulnerability to **read or write arbitrary memory locations** (via **format specifiers** like %s), potentially leading to information disclosure or code execution. **Always** write the format string as a constant in the program, as the malicious input will be treated as data. Similar happens with parent-child processes and libraries with environment variables.
**Command Injection**: Occurs when user input is passed to a system command **without** proper validation or sanitization. An attacker can exploit this vulnerability to execute **arbitrary commands** on the host operating system, potentially leading to unauthorized access or data compromise. **Always** validate and sanitize user input before passing it to system commands, and consider using safer alternatives like parameterized queries or APIs that do not invoke the shell.

### Metadata and Metacharacters

**Metadata** can be represented **in-band** (with a special character to determine termination, C) or **out-of-band** (number of characters is metadata stored separately from the characters, Java).

Vulnerability occurs when program **trusts input** to only contain characters (no metacharacters). Appear when constructing commands, queries, file paths, etc. Sanitize by whitelisting acceptable characters or if not possible blacklisting known dangerous characters.

**Embedded delimiters**: when input contains special characters that are used to separate data fields (e.g., commas in CSV files). An attacker can exploit this vulnerability by injecting additional delimiters, causing the program to misinterpret the input data. Sanitize by escaping or removing embedded delimiters from user input.

**NULL character termination**: occurs when user input contains NULL characters (ASCII 0) that are used to terminate strings in C/C++. An attacker can exploit this vulnerability by injecting NULL characters into the input, causing the program to truncate the input prematurely. Sanitize by removing or escaping NULL characters from user input.

**Separator injection**: occurs when user input is used to construct file paths or URLs without proper validation. An attacker can exploit this vulnerability by injecting path traversal characters (e.g., "../") or URL separators (e.g., "&") into the input, allowing them to access unauthorized files or resources. Sanitize by validating and normalizing file paths (firstly canonicallizing them) and URLs before using them in the program.

## Web Vulnerabilities

### A1 Broken Access Control

**Broken Access Control** (**BAC**): Occurs when a web application fails to properly enforce access control policies, allowing unauthorized users to access restricted resources or perform actions they should not be allowed to. This can lead to data breaches, privilege escalation, and other security issues. Mitigate by implementing proper access control mechanisms, such as role-based access control (RBAC) or attribute-based access control (ABAC), and regularly testing for access control vulnerabilities.

**DIOR** (**Direct Object Reference**): Occurs when a web application exposes internal object references (e.g., database keys, file names) to users without proper access control checks. An attacker can exploit this vulnerability by manipulating the object references to access unauthorized resources. Mitigate by using indirect references (e.g., mapping internal references to external identifiers) and implementing proper access control checks for all object access requests.

**Missing Function-Level** Access Control: Occurs when a web application "hides" certain functions or features from the user interface but does not enforce access control checks on the server side. An attacker can exploit this vulnerability by directly accessing the hidden functions or features, potentially leading to unauthorized actions or data access. Mitigate by not implementing "hidden" pages or functions as a form of protection.

**CORS** (**Cross-Origin Resource Sharing**) Misconfiguration: Occurs when a web application improperly configures **CORS** settings, allowing unauthorized domains to access its resources. An attacker can exploit this vulnerability by making cross-origin requests to the application, potentially leading to data theft or unauthorized actions. Mitigate by carefully configuring **CORS** settings to only allow trusted domains as well as **CORS**' configuration itself.

In sum:

- **Deny** by default, except public resources.
- Implement access control mechanisms **once** and **reuse** them.
- **Enforce** record ownership.
- **Disable** web server directory listing and ensure metadata does **not** leak sensitive information.
- **Log** access control failures and **alert** on anomalies.
- Stateful session identifiers should be **invalidated** on the server **after** logout.
- **Rate limit** API calls.

### A2 Cryptographic Failures

**Example 1**: credit card numbers stored in plaintext in a database, decrypted when needed. If the database is compromised, attackers can easily access the sensitive data.

**Example 2**: TLS not used for all pages. Attackers can monitor and intercept sensitive data transmitted between the client and server.

**Example 3**: database uses unsalted or simple hashes to store sensitive data. Attackers can use precomputed tables (rainbow tables) to quickly crack the hashes and access the sensitive data.

In sum:

- **Discard** unnecessary sensitive data **as soon as possible**
- **Encrypt** all sensitive data **while** stored and in transit.
- Use **strong** standard algorithms, protocols and keys.
- **Disable** caching for sensitive data.
- **Verify** independently all cryptographic implementations and configurations.

### A3 Injection

**Example 1**: **SQL** Injection. An attacker can manipulate a **SQL** query by injecting malicious input, allowing them to access or modify sensitive data in the database.

**Example 2**: **XML** Injection. An attacker can manipulate an **XML** document by injecting malicious input, allowing them to access or modify sensitive data or execute arbitrary code.

**Example 3**: **Command** Injection. An attacker can manipulate a system command by injecting malicious input, allowing them to execute arbitrary commands on the host operating system.

**Example 4**: **Cross Site Scripting** (**XSS**). Types:

- **Reflected XSS**: malicious script is reflected off a web server (e.g., in an error message or search result) and executed when a user clicks on a crafted link. Can be used to get session cookies, deface websites, or redirect users to malicious sites.
- **Stored XSS**: malicious script is permanently stored on the target server (e.g., in a database) and executed when a user accesses the affected page.
- **DOM-based XSS**: malicious script is executed as a result of modifying the **DOM** environment in the victim's browser (e.g., via client-side JavaScript).

**Example 5**: **CRLF Injection**. An attacker can manipulate HTTP headers by injecting carriage return (**CR**) and line feed (**LF**) characters, allowing them to perform HTTP response splitting attacks or manipulate cookies. Mitigate by avoiding OR validating and sanitizing user input before using it in HTTP headers, detect via common attack patterns.

**Example 6**: **Cross-Site Request Forgery** (**CSRF**). An attacker tricks a victim into submitting a request to a web application where the victim is authenticated, allowing the attacker to perform unauthorized actions on behalf of the victim. Mitigate by using anti-CSRF tokens, validating the **Referer** header, and requiring re-authentication for sensitive actions.

### A4 Insecure Design

Flaws related to **design and architectural** decisions, such as **lack of threat modeling**, **secure design patterns**, and **security controls**. These flaws can lead to vulnerabilities that are difficult to mitigate through traditional security measures. Insecure design != insecure implementation.

**Example 1**: credential recovery mechanisms that are weak or easily guessable, allowing attackers to gain unauthorized access to user accounts.

**Example 2**: booking discount system that allows group of users to repeatedly apply the same discount code, leading to significant financial losses.

In sum:

- **Secure** design patterns and principles.
- Library of **secure** design patterns.
- Threat **modeling** during design phase.
- **Unit and integration** tests for business logic.
- Segregate users **robustly**.
- **Limit** resource consumption per user or service.

### A5 Security Misconfiguration

**Example 1**: **XML External Entity** (**XXE**) Attack. An attacker can exploit a misconfigured **XML** parser that allows external entity references, leading to sensitive data disclosure, server-side request forgery (**SSRF**), or denial of service (**DoS**) attacks via editing the **XML** input.

In sum:

- **Hardening** the systems guidelines.
- Scanners and automated tools to **detect** misconfigurations.
- **Apply** minimal platform without unnecessary features.
- **Segmented** application architecture.

### A6 Vulnerable and Outdated Components

In sum:

- **Remove** unused dependencies, features, files and documentation.
- **Monitor** the security of all components, keeping them up-to-date.
- **Add** security wrappers to components when possible.

### A7 Identification and Authentication Failures

Weakness in implementation of identification and authentication mechanisms, allowing attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users' identities temporarily or permanently.

**Example 1**: **Credential Stuffing Attack**. An attacker uses a list of compromised usernames and passwords from a previous data breach to gain unauthorized access to user accounts on a different application that does not enforce strong password policies or multi-factor authentication (**MFA**).

**Example 2**: **Credential Spraying Attack**. An attacker attempts to gain unauthorized access to user accounts by systematically trying a small number of commonly used passwords across a large number of usernames, exploiting weak password policies and the absence of account lockout mechanisms.

**Example 3**: **Managing User Sessions**. An attacker exploits weak session management practices, such as using predictable session IDs or failing to invalidate sessions upon logout, to hijack user sessions and gain unauthorized access to sensitive information or perform actions on behalf of the user.

**Example 4**: **Session Hijacking**. An attacker intercepts a valid session token (e.g., via network sniffing or cross-site scripting) and uses it to impersonate the legitimate user, gaining unauthorized access to their account and sensitive data.

In sum:

- Multi-factor authentication (**MFA**).
- **Strong** password policies.
- **HTTPS** for all communications.
- **Avoid** own method to keep session management

### A8 Software and Data Integrity Failures

Failures related to code and infrastructure that do **not** protect against **integrity violations**. Examples include using untrusted CI/CD pipelines, relying on unverified software libraries, and insufficiently protecting data integrity.

**Example 1** **Insecure Deserialization**. An attacker exploits vulnerabilities in the deserialization process to manipulate serialized data, leading to remote code execution, privilege escalation, or denial of service attacks.

In sum:

- Use **digital signatures** to verify software and data integrity.
- Ensure updates come from **trusted** sources.
- **Verify and test** arriving components for security.
- **Review** process for code and configuration.
- Implement integrity checks or encryption of the **serialized** objects.

### A9 Security Logging and Monitoring Failures

Insufficient logging and monitoring, coupled with missing or ineffective integration with incident response, allows attackers to further attack systems, maintain persistence, pivot to more systems, and tamper, extract, or destroy data.

In sum:

- **Log all** relevant error conditions.
- High value operations need to have an **audit trail** that **cannot** be erased.
- High value operations have an **audit trail** with **integrity** controls to prevent tampering.
- Adopt accident **response and recovery procedures**.

### A10 Server-Side Request Forgery (SSRF)

**Cross-Site Request Forgery** (**SSRF**) occurs when a web application fetches a remote resource without validating the user-supplied URL. This allows an attacker to coerce the application to send requests to unintended locations, including internal systems that are not directly accessible from the outside.

In sum:

- **segment** remote resource access functionality in separate networks to **reduce**
the impact.
- **enforce** deny-by-default policies to block all but **essential** intranet traffic.
- **sanitize** and **validate** all client-supplied input data.
- **disable** HTTP redirections.

## Database Vulnerabilities

**SQL Injection**: An attacker can manipulate a SQL query by injecting malicious input, allowing them to access or modify sensitive data in the database. Mitigate by using prepared statements with parameterized queries, which separate SQL code from data, preventing attackers from altering the query structure. Can be **first-order** (input is directly used in the query) or **second-order** (input is stored and later used in a query).

**Example 1** Tautology-based Injection. An attacker injects a condition that is always true (e.g., ' OR '1'='1) into a SQL query, allowing them to bypass authentication or retrieve all records from a database table.

**Example 2** Union-based Injection. An attacker uses the UNION SQL operator to combine the results of a legitimate query with the results of a malicious query, allowing them to retrieve additional data from other database tables.

**Example 3** Piggybacked Queries. An attacker appends a malicious SQL query to a legitimate query using a semicolon (';'), allowing them to execute multiple queries in a single request.

**Example 4** Stored Procedure Injection. An attacker exploits vulnerabilities in stored procedures by injecting malicious input, allowing them to execute arbitrary SQL commands or manipulate data within the database.

**Example 5** Illegal/Incorrect Query. An attacker injects an input that causes an SQL error, which may reveal sensitive information about the database structure or application logic.

**Example 6** Inference-based Injection. An attacker uses boolean conditions or time delays to infer information about the database structure or data, even when direct data retrieval is not possible.

**Example 7** Alternate Encodings. An attacker uses alternate encodings (e.g., hexadecimal, Unicode) to obfuscate their SQL injection payloads, bypassing input validation mechanisms.

In sum:

- **Parameterized** queries.
- **Whitelisting** input validation.
- Input **type checking**.
- **Encoding** to something that can be **trusted**.

## Static Code Analysis

Code is **not** executed, but **analyzed** for patterns that may lead to vulnerabilities. Can be done **manually** (code reviews) or **automatically** (static analysis tools). Can find issues like buffer overflows, SQL injection vulnerabilities, insecure cryptographic practices, and more. Helps identify potential security flaws early in the development process, allowing developers to address them before they can be exploited.

Composed by a database of known vulnerability patterns, a **code preprocessor** to check what is really compiled, and a lexical analyzer to parse the code and look for patterns.

Benefits:

- **Verifies** code thoroughly and consistently.
- Leads to **root** of the problem.
- Can find problems **early** in the development process.
- If a new type of vulnerability is **discovered**, the tool can be **updated** to check for it in existing codebases.
- Can be used to find **other** types of bugs, not **just** security vulnerabilities.

Limitations:

- May produce **false positives** (**flagging non-issues**) and **false negatives** (**missing real issues**).
- May not **fully** understand the context or intent of the code.
- May struggle with **complex code structures** or **dynamic features** of programming languages.
- Tries to solve a **computationally hard problem** (halting problem).

### Semantic Analysis

**Syntax Tree**: A tree representation of the syntactic structure of source code, where each node represents a construct occurring in the source code. It is used in static code analysis to understand the hierarchical structure of the code and identify patterns that may lead to vulnerabilities.

**Abstract Syntax Tree (AST)**: A simplified version of the syntax tree that abstracts away certain details of the source code, focusing on the essential structure and semantics. It is used in static code analysis to facilitate the identification of potential security issues by providing a more manageable representation of the code.

**Type checking analysis**: A static code analysis technique that verifies the consistency of data types in a program. It ensures that variables and expressions are used in a manner consistent with their declared types, helping to identify potential type-related vulnerabilities or errors.

**Control-flow analysis**: A static code analysis technique that examines the flow of control within a program, identifying the possible paths that execution can take. It helps to identify potential vulnerabilities related to control flow, such as unreachable code, infinite loops, or improper handling of exceptions.

**Data-flow analysis**: A static code analysis technique that tracks the flow of data through a program, identifying how data is defined, used, and modified. It helps to identify potential vulnerabilities related to data handling, such as uninitialized variables, data leaks, or improper sanitization of user input.

**Example 1** WAP (Web Application Protection): A static code analysis tool that scans web application source code for security vulnerabilities, such as SQL injection, cross-site scripting (XSS), and insecure configuration settings. It provides developers with detailed reports and recommendations for fixing identified issues.

## Software Testing

Challenges:

- **Observability**: easiness of observing the internal state of the system.
- **Controllability**: easiness of controlling the inputs to the system.
- **Coverage**: capability of testing all possible execution paths.

### Security vs Traditional Testing

Functional testing: verifies that the system behaves as expected for valid inputs.
Security testing: verifies that the system behaves securely for invalid inputs.

**Black-box** testing: tester has no knowledge of the internal workings of the system.
**Gray-box** testing: tester has partial knowledge of the internal workings of the system.
**White-box** testing: tester has full knowledge of the internal workings of the system.

### Fuzz Testing

Knowledge of target:

- **Thin fuzzers**: little knowledge of the system, generate random inputs to test for crashes or unexpected behavior.
- **Fat fuzzers**: more knowledge of the system, generate inputs based on the structure and format of the expected input data, but irregular or unexpected inputs.

Specialization:

- **Specialized**: designed for specific types of applications or protocols (e.g., web applications, network protocols).
- **Generic**: can be used to test a wide range of applications and protocols.

Access to code:

- **Black**: no access to the internal workings of the system, goes through the interface.
- **Gray**: ability to compile, eventually adding instrumentation code.
- **White**: the execution of the application is emulated, looking for conditions
in the input that would cause a failure

**Blind fuzzers** have **limited** knowledge about the source of the target, but try to **generate** inputs that cause a crash. Types:

- **mutational fuzzers**: start with a set of valid inputs and mutate them to create new test cases.
- **generational fuzzers**: generate inputs from scratch based on a predefined grammar or specification.

Coverage-guided fuzzers use **feedback** from the target application to guide the generation of n**ew test cases**, aiming to **maximize** code coverage and explore **new** execution paths.

**Hybrid fuzzers** combine multiple techniques, such as mutation, generation, and coverage guidance, to improve the effectiveness of the fuzzing process.

**Example 1** **SPIKE**: A popular open-source fuzz testing framework that allows testers to create custom fuzzers for various protocols and applications. It provides a flexible architecture for generating test cases and monitoring the target application's behavior during testing.

**Example 2** **AFL** (**American Fuzzy Loop**): A widely used coverage-guided fuzz testing tool that employs genetic algorithms to evolve test cases based on code coverage feedback. It is known for its effectiveness in discovering vulnerabilities in various software applications.

### Dynamic Taint Analysis

**Runtime technique** that **tracks the flow of data** through a program, identifying how **tainted** (untrusted) data is propagated and used. Helps to identify **potential** vulnerabilities related to data handling, such as SQL injection, cross-site scripting (XSS), and buffer overflows.
Taint sinks are operations that can lead to security vulnerabilities if they process **tainted** data (e.g., executing a SQL query with user input). Taint sources are points where untrusted data enters the program (e.g., user input from a web form). Taint propagation rules define how taint is transferred between variables and data structures as the program executes.

### Vulnerability Scanners

**Automated tools** that scan software applications for known vulnerabilities, misconfigurations, and security issues. They typically use a database of known vulnerability signatures and patterns to identify potential security flaws in the target application. Vulnerability scanners can be used to assess the security posture of web applications, network services, and operating systems.

### Proxies

**Intercepting proxies** are tools that sit between a client and a server, allowing testers to **capture**, **modify**, and **analyze** the communication between the two. They are commonly used in web application security testing to identify vulnerabilities such as **SQL injection**, **Cross-Site Scripting** (XSS), and **insecure session management**. By intercepting and manipulating requests and responses, testers can explore how the application handles various inputs and identify potential security weaknesses.

**Example 1** **ZAP**: (**Zed Attack Proxy**): An open-source intercepting proxy developed by OWASP that provides a comprehensive set of tools for web application security testing. It allows testers to capture and modify HTTP/HTTPS traffic, perform automated vulnerability scans, and analyze the security of web applications.

## Race Conditions

### TOCTOU

**Time Of Check To Time Of Use** (**TOCTOU**) is a type of **race** condition that occurs when a program checks a condition (e.g., file permissions) and then uses the result of that check at a later time. If an attacker can change the state of the system between the check and the use, they can exploit the vulnerability to gain unauthorized access or perform malicious actions.

**Memory** races occur when multiple threads access **shared memory concurrently**, and at least **one** thread modifies the memory. This can lead to inconsistent or unexpected results if the threads are not properly **synchronized**.

**File** race conditions occur when multiple processes access a **shared file concurrently**, and at least **one** process modifies the file. This can lead to data corruption or unauthorized access if the processes are not properly **synchronized**.

**Permission** races occur when a program checks the **permissions** of a resource (e.g., file, network socket) and then uses the resource at a **later** time. If an attacker can change the **permissions** of the resource **between the check and the use**, they can exploit the vulnerability to gain unauthorized access or perform malicious actions.

**Temporary** file races occur when a program creates a temporary file and then uses it at a **later** time. If an attacker can create a file with the **same name** as the **temporary file** before the program uses it, they can exploit the vulnerability to gain unauthorized access or perform malicious actions.

In sum:

- Use **atomic** operations that **combine** the check and use into a single step.
- Use **file locking mechanisms** to prevent **concurrent** access to shared resources.
- **Minimize** the time **between the check and use** to reduce the window of opportunity for an attacker.
- **Validate** the **state** of the system again **before** using the result of the check.

### Concurrency

In sum:

- Use **synchronization mechanisms** (e.g., mutexes, semaphores) to **control** access to **shared** resources.
- **Minimize** the use of **shared** resources to reduce the potential for race conditions.
- Use **immutable data structures** where possible to **avoid** shared mutable state.
- Use **signals or events** to coordinate actions **between** threads or processes.

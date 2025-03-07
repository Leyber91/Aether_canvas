# AI Canvas System Architecture: Complete File Structure

## Shared Infrastructure (SI)

### SI-01: Communication Bridge
#### SI-01.1: `shared/event_bus.js`
- **Description**: Frontend event bus implementing publish/subscribe pattern
- **Inputs**: Event topics, event payloads (any JSON-serializable data)
- **Outputs**: Event notifications to subscribers
- **Key Functions**:
  - `subscribe(topic, callback)` → subscription ID
  - `publish(topic, payload)` → boolean success
  - `unsubscribe(subscriptionId)` → boolean success

#### SI-01.2: `shared/event_bus.py`
- **Description**: Backend event bus implementing publish/subscribe pattern
- **Inputs**: Event topics, event payloads (any JSON-serializable data)
- **Outputs**: Event notifications to subscribers
- **Key Functions**:
  - `subscribe(topic, callback)` → subscription ID
  - `publish(topic, payload)` → boolean success
  - `unsubscribe(subscription_id)` → boolean success

#### SI-01.3: `shared/websocket_manager.js`
- **Description**: Frontend WebSocket connection manager
- **Inputs**: WebSocket URL, message handlers, connection options
- **Outputs**: Established WebSocket connections, streaming messages
- **Key Functions**:
  - `connect(url, options)` → connection object
  - `send(message)` → boolean success
  - `subscribe(event_type, callback)` → subscription ID
  - `close()` → boolean success

#### SI-01.4: `shared/websocket_manager.py`
- **Description**: Backend WebSocket handler and connection manager
- **Inputs**: WebSocket connections, client messages
- **Outputs**: Server messages, streaming responses
- **Key Functions**:
  - `register_handler(event_type, handler)` → handler ID
  - `broadcast(event_type, payload)` → boolean success
  - `send_to_client(client_id, payload)` → boolean success
  - `create_stream_response(generator)` → stream response object

### SI-02: Configuration & Constants
#### SI-02.1: `shared/config.js`
- **Description**: Frontend configuration manager
- **Inputs**: Environment variables, config files
- **Outputs**: Configuration values
- **Key Functions**:
  - `getConfig(key, defaultValue)` → config value
  - `isFeatureEnabled(featureKey)` → boolean
  - `getEnvironment()` → string environment name

#### SI-02.2: `shared/config.py`
- **Description**: Backend configuration manager
- **Inputs**: Environment variables, config files
- **Outputs**: Configuration values
- **Key Functions**:
  - `get_config(key, default_value=None)` → config value
  - `is_feature_enabled(feature_key)` → boolean
  - `get_environment()` → string environment name

#### SI-02.3: `shared/constants.js`
- **Description**: Frontend constants and enumerations
- **Inputs**: None
- **Outputs**: Constant values and enum types
- **Key Exports**:
  - `NodeTypes` enum
  - `EdgeTypes` enum
  - `MessageRoles` enum
  - `API_ENDPOINTS` object

#### SI-02.4: `shared/constants.py`
- **Description**: Backend constants and enumerations
- **Inputs**: None
- **Outputs**: Constant values and enum types
- **Key Exports**:
  - `NodeTypes` enum
  - `EdgeTypes` enum
  - `MessageRoles` enum
  - `ExecutionStatus` enum

### SI-03: Shared Utilities
#### SI-03.1: `shared/error_utils.js`
- **Description**: Frontend error handling utilities
- **Inputs**: Error objects, error contexts
- **Outputs**: Standardized error objects
- **Key Functions**:
  - `createError(code, message, context)` → error object
  - `isNetworkError(error)` → boolean
  - `isAuthError(error)` → boolean
  - `formatErrorMessage(error)` → string

#### SI-03.2: `shared/errors.py`
- **Description**: Backend error classes and handling utilities
- **Inputs**: Error contexts, error messages
- **Outputs**: Custom error types
- **Key Classes**:
  - `BaseCanvasError` class
  - `ValidationError` class
  - `AuthorizationError` class
  - `ResourceNotFoundError` class

#### SI-03.3: `shared/utils.js`
- **Description**: Frontend common utility functions
- **Inputs**: Various data
- **Outputs**: Transformed data
- **Key Functions**:
  - `debounce(fn, delay)` → debounced function
  - `deepClone(obj)` → cloned object
  - `formatDate(date, format)` → formatted date string
  - `validateSchema(data, schema)` → validation result

#### SI-03.4: `shared/utils.py`
- **Description**: Backend common utility functions
- **Inputs**: Various data
- **Outputs**: Transformed data
- **Key Functions**:
  - `deep_merge(dict1, dict2)` → merged dictionary
  - `format_datetime(dt, format_str)` → formatted date string
  - `validate_schema(data, schema)` → validation result
  - `generate_unique_id(prefix)` → unique ID string

## Frontend Architecture (FE)

### FE-01: Core Infrastructure
#### FE-01.1: `frontend/store/index.js`
- **Description**: Redux store configuration
- **Inputs**: Reducer slices, middleware options
- **Outputs**: Configured Redux store
- **Key Functions**:
  - `configureStore()` → Redux store

#### FE-01.2: `frontend/store/reducers/graphSlice.js`
- **Description**: Graph state management slice
- **Inputs**: Graph data, action payloads
- **Outputs**: Updated graph state
- **Key Exports**:
  - `graphReducer` reducer
  - `addNode`, `updateNode`, `removeNode` actions
  - `addEdge`, `updateEdge`, `removeEdge` actions
  - `selectGraph`, `updateGraph` actions

#### FE-01.3: `frontend/store/reducers/workflowSlice.js`
- **Description**: Workflow execution state management slice
- **Inputs**: Execution data, action payloads
- **Outputs**: Updated workflow state
- **Key Exports**:
  - `workflowReducer` reducer
  - `startExecution`, `pauseExecution`, `stopExecution` actions
  - `updateExecutionStatus`, `setExecutionResults` actions

#### FE-01.4: `frontend/store/reducers/chatSlice.js`
- **Description**: Chat and conversation state management slice
- **Inputs**: Conversation data, action payloads
- **Outputs**: Updated chat state
- **Key Exports**:
  - `chatReducer` reducer
  - `addMessage`, `updateMessage`, `clearConversation` actions
  - `setActiveConversation`, `appendStreamChunk` actions

#### FE-01.5: `frontend/store/selectors/graphSelectors.js`
- **Description**: Graph state selectors
- **Inputs**: Redux state
- **Outputs**: Derived graph data
- **Key Exports**:
  - `selectAllNodes`, `selectNodeById` selectors
  - `selectAllEdges`, `selectEdgeById` selectors
  - `selectGraphMetadata`, `selectGraphLayout` selectors

#### FE-01.6: `frontend/store/selectors/workflowSelectors.js`
- **Description**: Workflow state selectors
- **Inputs**: Redux state
- **Outputs**: Derived workflow data
- **Key Exports**:
  - `selectExecutionStatus`, `selectExecutionResults` selectors
  - `selectNodeResults`, `selectExecutionHistory` selectors

#### FE-01.7: `frontend/store/selectors/chatSelectors.js`
- **Description**: Chat state selectors
- **Inputs**: Redux state
- **Outputs**: Derived chat data
- **Key Exports**:
  - `selectActiveConversation`, `selectMessages` selectors
  - `selectMessageById`, `selectIsTyping` selectors

#### FE-01.8: `frontend/api/api_client.js`
- **Description**: HTTP client with interceptors
- **Inputs**: API requests, configuration
- **Outputs**: API responses
- **Key Functions**:
  - `get(url, config)` → Promise<response>
  - `post(url, data, config)` → Promise<response>
  - `put(url, data, config)` → Promise<response>
  - `delete(url, config)` → Promise<response>

#### FE-01.9: `frontend/api/graphApi.js`
- **Description**: Graph-related API services
- **Inputs**: Graph data, request parameters
- **Outputs**: API responses for graph operations
- **Key Functions**:
  - `getGraphs()` → Promise<graphs[]>
  - `getGraphById(id)` → Promise<graph>
  - `createGraph(graphData)` → Promise<newGraph>
  - `updateGraph(id, graphData)` → Promise<updatedGraph>
  - `deleteGraph(id)` → Promise<success>
  - `getNodes(graphId)` → Promise<nodes[]>
  - `createNode(graphId, nodeData)` → Promise<newNode>
  - `updateNode(nodeId, nodeData)` → Promise<updatedNode>
  - `deleteNode(nodeId)` → Promise<success>
  - `createEdge(graphId, edgeData)` → Promise<newEdge>
  - `deleteEdge(edgeId)` → Promise<success>

#### FE-01.10: `frontend/api/workflowApi.js`
- **Description**: Workflow-related API services
- **Inputs**: Execution parameters, graph IDs
- **Outputs**: API responses for workflow operations
- **Key Functions**:
  - `executeGraph(graphId, options)` → Promise<executionId>
  - `getExecutionStatus(executionId)` → Promise<status>
  - `getExecutionResults(executionId)` → Promise<results>
  - `stopExecution(executionId)` → Promise<success>
  - `getExecutionHistory(graphId)` → Promise<history[]>

#### FE-01.11: `frontend/api/chatApi.js`
- **Description**: Chat-related API services
- **Inputs**: Conversation data, message content
- **Outputs**: API responses for chat operations
- **Key Functions**:
  - `getConversations(nodeId)` → Promise<conversations[]>
  - `getMessages(conversationId)` → Promise<messages[]>
  - `sendMessage(conversationId, content)` → Promise<message>
  - `streamMessage(conversationId, content)` → EventSource
  - `createConversation(nodeId)` → Promise<conversation>

#### FE-01.12: `frontend/api/handlers.js`
- **Description**: API error and response handlers
- **Inputs**: API responses, errors
- **Outputs**: Standardized responses, error handling
- **Key Functions**:
  - `handleResponse(response)` → processed response
  - `handleError(error)` → standardized error
  - `retryRequest(request, maxRetries)` → Promise<response>

### FE-02: Graph Editor Module
#### FE-02.1: `frontend/graph/cytoscape_manager.js`
- **Description**: Cytoscape.js integration manager
- **Inputs**: Graph data, container element, options
- **Outputs**: Cytoscape instance, graph visualizations
- **Key Functions**:
  - `initialize(container, options)` → cytoscape instance
  - `renderGraph(graphData)` → rendered graph
  - `applyLayout(layoutName)` → laid out graph
  - `exportImage(format)` → image data

#### FE-02.2: `frontend/graph/node_manager.js`
- **Description**: Node creation and management
- **Inputs**: Node data, user interactions
- **Outputs**: Node operations, UI updates
- **Key Functions**:
  - `createNode(nodeData)` → new node
  - `editNode(nodeId, updates)` → updated node
  - `deleteNode(nodeId)` → success boolean
  - `getNodeConnections(nodeId)` → connections array

#### FE-02.3: `frontend/graph/edge_manager.js`
- **Description**: Edge management and validation
- **Inputs**: Edge data, user interactions
- **Outputs**: Edge operations, validation results
- **Key Functions**:
  - `createEdge(sourceId, targetId, type)` → new edge
  - `validateConnection(sourceId, targetId)` → validation result
  - `getAvailableEdgeTypes(sourceId, targetId)` → types array
  - `deleteEdge(edgeId)` → success boolean

#### FE-02.4: `frontend/graph/layout_manager.js`
- **Description**: Graph layout management
- **Inputs**: Graph data, layout options
- **Outputs**: Positioned graph elements
- **Key Functions**:
  - `applyLayout(layoutName, options)` → positioned graph
  - `savePositions()` → position data
  - `restorePositions(positionData)` → restored graph
  - `centerOnNode(nodeId)` → centered view

#### FE-02.5: `frontend/graph/graph_history.js`
- **Description**: Graph editing history for undo/redo
- **Inputs**: Graph operations
- **Outputs**: History states, undo/redo operations
- **Key Functions**:
  - `recordAction(action)` → action record
  - `undo()` → previous state
  - `redo()` → next state
  - `getHistoryState()` → history state object

### FE-03: Workflow & Chat Modules
#### FE-03.1: `frontend/workflow/execution_controller.js`
- **Description**: Workflow execution controller
- **Inputs**: Graph ID, execution options
- **Outputs**: Execution control, status updates
- **Key Functions**:
  - `executeGraph(graphId, options)` → execution object
  - `pauseExecution()` → success boolean
  - `resumeExecution()` → success boolean
  - `stopExecution()` → success boolean
  - `monitorStatus(callback)` → monitor handle

#### FE-03.2: `frontend/workflow/result_view.js`
- **Description**: Execution result visualization
- **Inputs**: Execution results data
- **Outputs**: Rendered results, visualizations
- **Key Functions**:
  - `renderResults(executionResults)` → rendered component
  - `highlightNode(nodeId)` → highlighted node
  - `getNodeResult(nodeId)` → node result data
  - `exportResults(format)` → exported results

#### FE-03.3: `frontend/workflow/execution_history.js`
- **Description**: Execution history management
- **Inputs**: Execution records
- **Outputs**: History views, comparisons
- **Key Functions**:
  - `loadHistory(graphId)` → history records
  - `compareExecutions(id1, id2)` → comparison data
  - `replayExecution(executionId)` → replay controller
  - `exportHistory(format)` → exported history

#### FE-03.4: `frontend/chat/conversation_manager.js`
- **Description**: Conversation state management
- **Inputs**: Conversation data, node context
- **Outputs**: Conversation operations, history
- **Key Functions**:
  - `createConversation(nodeId)` → new conversation
  - `loadConversation(conversationId)` → loaded conversation
  - `sendMessage(content)` → sent message
  - `clearConversation()` → success boolean
  - `exportConversation(format)` → exported conversation

#### FE-03.5: `frontend/chat/message_view.js`
- **Description**: Message rendering component
- **Inputs**: Message data, formatting options
- **Outputs**: Rendered messages with formatting
- **Key Functions**:
  - `renderMessage(message)` → rendered component
  - `renderMarkdown(content)` → rendered markdown
  - `renderCodeBlock(code, language)` → rendered code
  - `renderAttachment(attachment)` → rendered attachment

#### FE-03.6: `frontend/chat/stream_handler.js`
- **Description**: Stream processing for chat
- **Inputs**: Stream sources, message chunks
- **Outputs**: Processed stream data, partial updates
- **Key Functions**:
  - `startStream(source)` → stream controller
  - `processChunk(chunk)` → processed chunk
  - `handleStreamError(error)` → error handling
  - `endStream()` → finalized message

### FE-04: UI Component Library
#### FE-04.1: `frontend/components/ui/Button.js`
- **Description**: Reusable button component
- **Inputs**: Props (variant, size, onClick, children, etc.)
- **Outputs**: Rendered button component
- **Key Variants**: Primary, Secondary, Danger, Ghost

#### FE-04.2: `frontend/components/ui/Input.js`
- **Description**: Reusable input component
- **Inputs**: Props (type, value, onChange, error, etc.)
- **Outputs**: Rendered input component
- **Key Variants**: Text, Number, Password, Textarea

#### FE-04.3: `frontend/components/ui/Modal.js`
- **Description**: Reusable modal dialog component
- **Inputs**: Props (isOpen, onClose, title, children, etc.)
- **Outputs**: Rendered modal component
- **Key Features**: Different sizes, confirmation options

#### FE-04.4: `frontend/components/ui/index.js`
- **Description**: UI component exports
- **Inputs**: None
- **Outputs**: Exported UI components
- **Key Exports**: All UI components for easy imports

#### FE-04.5: `frontend/components/graph/NodeComponent.js`
- **Description**: Graph node UI component
- **Inputs**: Props (nodeData, isSelected, onClick, etc.)
- **Outputs**: Rendered node component
- **Key Features**: Different node types, selection states

#### FE-04.6: `frontend/components/graph/EdgeComponent.js`
- **Description**: Graph edge UI component
- **Inputs**: Props (edgeData, isSelected, etc.)
- **Outputs**: Rendered edge component
- **Key Features**: Different edge types, connection states

#### FE-04.7: `frontend/components/workflow/ExecutionPanel.js`
- **Description**: Workflow execution control panel
- **Inputs**: Props (graphId, executionStatus, etc.)
- **Outputs**: Rendered execution panel
- **Key Features**: Execution controls, status indicators

#### FE-04.8: `frontend/components/chat/MessageComponent.js`
- **Description**: Chat message component
- **Inputs**: Props (message, isUser, isStreaming, etc.)
- **Outputs**: Rendered message component
- **Key Features**: User/assistant messages, markdown rendering

## Backend Architecture (BE)

### BE-01: API Layer
#### BE-01.1: `backend/api/blueprints/graph_routes.py`
- **Description**: Graph API routes
- **Inputs**: HTTP requests with graph data
- **Outputs**: JSON responses with graph operations results
- **Key Routes**:
  - `GET /api/graphs` → list of graphs
  - `POST /api/graphs` → create graph
  - `GET /api/graphs/<id>` → graph details
  - `PUT /api/graphs/<id>` → update graph
  - `DELETE /api/graphs/<id>` → delete graph
  - `GET /api/graphs/<id>/nodes` → list of nodes
  - `POST /api/graphs/<id>/nodes` → create node
  - `GET /api/nodes/<id>` → node details
  - `PUT /api/nodes/<id>` → update node
  - `DELETE /api/nodes/<id>` → delete node
  - `POST /api/graphs/<id>/edges` → create edge
  - `DELETE /api/edges/<id>` → delete edge

#### BE-01.2: `backend/api/blueprints/workflow_routes.py`
- **Description**: Workflow execution API routes
- **Inputs**: HTTP requests with execution parameters
- **Outputs**: JSON responses with execution results
- **Key Routes**:
  - `POST /api/graphs/<id>/execute` → start execution
  - `GET /api/executions/<id>` → execution status
  - `GET /api/executions/<id>/results` → execution results
  - `POST /api/executions/<id>/stop` → stop execution
  - `GET /api/graphs/<id>/executions` → execution history

#### BE-01.3: `backend/api/blueprints/chat_routes.py`
- **Description**: Conversation and chat API routes
- **Inputs**: HTTP requests with message data
- **Outputs**: JSON responses, streaming responses
- **Key Routes**:
  - `GET /api/nodes/<id>/conversations` → list conversations
  - `POST /api/nodes/<id>/conversations` → create conversation
  - `GET /api/conversations/<id>/messages` → get messages
  - `POST /api/conversations/<id>/messages` → send message
  - `GET /api/conversations/<id>/messages/stream` → stream messages

#### BE-01.4: `backend/api/websocket_server.py`
- **Description**: WebSocket server implementation
- **Inputs**: WebSocket connections, messages
- **Outputs**: Real-time updates, streaming data
- **Key Functions**:
  - `handle_connection(client)` → connection handler
  - `process_message(client, message)` → message processor
  - `broadcast_update(topic, data)` → broadcast to clients
  - `send_to_client(client_id, message)` → targeted message

### BE-02: Service Layer
#### BE-02.1: `backend/services/graph_service.py`
- **Description**: Graph service facade
- **Inputs**: Graph operation requests
- **Outputs**: Graph operation results
- **Key Functions**:
  - `get_graphs()` → list of graphs
  - `get_graph_by_id(graph_id)` → graph details
  - `create_graph(graph_data)` → new graph
  - `update_graph(graph_id, updates)` → updated graph
  - `delete_graph(graph_id)` → operation result
  - `get_nodes(graph_id)` → list of nodes
  - `get_node_by_id(node_id)` → node details
  - `create_node(graph_id, node_data)` → new node
  - `update_node(node_id, updates)` → updated node
  - `delete_node(node_id)` → operation result
  - `create_edge(source_id, target_id, edge_type)` → new edge
  - `delete_edge(edge_id)` → operation result

#### BE-02.2: `backend/services/graph_crud_service.py`
- **Description**: Graph CRUD operations
- **Inputs**: Graph, node, edge data
- **Outputs**: Database operation results
- **Key Functions**:
  - `create_graph(name, description)` → graph object
  - `read_graph(graph_id)` → graph object
  - `update_graph(graph_id, updates)` → updated graph
  - `delete_graph(graph_id)` → boolean success
  - `create_node(graph_id, node_data)` → node object
  - `read_node(node_id)` → node object
  - `update_node(node_id, updates)` → updated node
  - `delete_node(node_id)` → boolean success
  - `create_edge(source_id, target_id, edge_type)` → edge object
  - `read_edge(edge_id)` → edge object
  - `delete_edge(edge_id)` → boolean success

#### BE-02.3: `backend/services/graph_analysis_service.py`
- **Description**: Graph analysis operations
- **Inputs**: Graph structure data
- **Outputs**: Analysis results
- **Key Functions**:
  - `build_networkx_graph(graph_id)` → NetworkX graph
  - `get_topological_sort(graph_id)` → ordered node list
  - `detect_cycles(graph_id)` → cycle information
  - `get_execution_order(graph_id)` → execution order list
  - `get_parent_nodes(node_id)` → parent nodes list
  - `get_child_nodes(node_id)` → child nodes list
  - `validate_graph(graph_id)` → validation results

#### BE-02.4: `backend/services/graph_template_service.py`
- **Description**: Graph template management
- **Inputs**: Template data, graph data
- **Outputs**: Template operations results
- **Key Functions**:
  - `save_as_template(graph_id, template_name)` → template object
  - `list_templates()` → templates list
  - `create_from_template(template_id)` → new graph
  - `export_graph(graph_id, format)` → exported graph data
  - `import_graph(data)` → imported graph

#### BE-02.5: `backend/services/execution_service.py`
- **Description**: Workflow execution orchestration
- **Inputs**: Graph ID, execution parameters
- **Outputs**: Execution results, status updates
- **Key Functions**:
  - `execute_workflow(graph_id, options)` → execution object
  - `execute_node(node_id, context)` → node result
  - `get_execution_status(execution_id)` → status object
  - `get_execution_results(execution_id)` → results object
  - `stop_execution(execution_id)` → boolean success
  - `propagate_context(node_id, result)` → updated context

#### BE-02.6: `backend/services/ollama_service.py`
- **Description**: Ollama API integration
- **Inputs**: Prompts, model parameters
- **Outputs**: AI model responses
- **Key Functions**:
  - `get_available_models()` → models list
  - `generate_completion(model, prompt, params)` → completion result
  - `generate_chat_completion(model, messages, params)` → chat completion
  - `stream_chat_completion(model, messages, params)` → streamed response
  - `process_node(node, context)` → processed node result

#### BE-02.7: `backend/services/groq_service.py`
- **Description**: Groq API integration
- **Inputs**: Prompts, model parameters
- **Outputs**: AI model responses
- **Key Functions**:
  - `get_available_models()` → models list
  - `generate_chat_completion(model, messages, params)` → chat completion
  - `stream_chat_completion(model, messages, params)` → streamed response
  - `process_node(node, context)` → processed node result
  - `handle_rate_limits()` → rate limit handler

#### BE-02.8: `backend/services/conversation_service.py`
- **Description**: Conversation management
- **Inputs**: Conversation data, messages
- **Outputs**: Conversation operations results
- **Key Functions**:
  - `get_conversations(node_id)` → conversations list
  - `get_conversation(conversation_id)` → conversation object
  - `create_conversation(node_id)` → new conversation
  - `get_messages(conversation_id)` → messages list
  - `add_message(conversation_id, role, content)` → new message
  - `get_conversation_context(conversation_id)` → context object
  - `export_conversation(conversation_id, format)` → exported data

### BE-03: Data Access Layer
#### BE-03.1: `backend/repositories/graph_repository.py`
- **Description**: Graph data repository
- **Inputs**: Graph data, queries
- **Outputs**: Database operation results
- **Key Functions**:
  - `find_all()` → all graphs list
  - `find_by_id(graph_id)` → graph object
  - `create(graph_data)` → new graph
  - `update(graph_id, updates)` → updated graph
  - `delete(graph_id)` → boolean success
  - `find_graphs_by_query(query)` → filtered graphs list

#### BE-03.2: `backend/repositories/node_repository.py`
- **Description**: Node data repository
- **Inputs**: Node data, queries
- **Outputs**: Database operation results
- **Key Functions**:
  - `find_by_graph_id(graph_id)` → nodes list
  - `find_by_id(node_id)` → node object
  - `create(node_data)` → new node
  - `update(node_id, updates)` → updated node
  - `delete(node_id)` → boolean success
  - `find_by_type(node_type)` → nodes list

#### BE-03.3: `backend/repositories/edge_repository.py`
- **Description**: Edge data repository
- **Inputs**: Edge data, queries
- **Outputs**: Database operation results
- **Key Functions**:
  - `find_by_graph_id(graph_id)` → edges list
  - `find_by_id(edge_id)` → edge object
  - `create(edge_data)` → new edge
  - `delete(edge_id)` → boolean success
  - `find_by_node(node_id, direction)` → connected edges list

#### BE-03.4: `backend/repositories/conversation_repository.py`
- **Description**: Conversation data repository
- **Inputs**: Conversation data, queries
- **Outputs**: Database operation results
- **Key Functions**:
  - `find_by_node_id(node_id)` → conversations list
  - `find_by_id(conversation_id)` → conversation object
  - `create(conversation_data)` → new conversation
  - `update(conversation_id, updates)` → updated conversation
  - `delete(conversation_id)` → boolean success
  - `find_messages(conversation_id)` → messages list
  - `add_message(message_data)` → new message

#### BE-03.5: `backend/repositories/execution_repository.py`
- **Description**: Execution data repository
- **Inputs**: Execution data, queries
- **Outputs**: Database operation results
- **Key Functions**:
  - `find_by_graph_id(graph_id)` → executions list
  - `find_by_id(execution_id)` → execution object
  - `create(execution_data)` → new execution
  - `update_status(execution_id, status)` → updated execution
  - `add_result(execution_id, node_id, result)` → new result
  - `get_results(execution_id)` → results list

#### BE-03.6: `backend/db/sqlalchemy_manager.py`
- **Description**: SQLAlchemy database manager
- **Inputs**: Database connection parameters
- **Outputs**: Database session, connection management
- **Key Functions**:
  - `init_db(app)` → initialized database
  - `get_session()` → database session
  - `create_tables()` → schema creation
  - `run_migrations()` → migration execution

#### BE-03.7: `backend/db/model_mappers.py`
- **Description**: ORM to domain model mappers
- **Inputs**: Database models, domain models
- **Outputs**: Mapped objects
- **Key Functions**:
  - `map_to_domain(db_model)` → domain model
  - `map_to_db(domain_model)` → database model
  - `map_collection(db_models)` → domain models list

#### BE-03.8: `backend/cache/redis_cache.py`
- **Description**: Redis cache implementation
- **Inputs**: Cache keys, values, expiration times
- **Outputs**: Cache operations results
- **Key Functions**:
  - `get(key)` → cached value
  - `set(key, value, expiry)` → boolean success
  - `delete(key)` → boolean success
  - `exists(key)` → boolean exists
  - `flush()` → boolean success

### BE-04: Infrastructure
#### BE-04.1: `backend/infrastructure/logger.py`
- **Description**: Logging configuration
- **Inputs**: Log messages, levels, contexts
- **Outputs**: Formatted logs
- **Key Functions**:
  - `setup_logging(config)` → configured logger
  - `get_logger(name)` → logger instance
  - `log_request(request)` → logged request
  - `log_error(error, context)` → logged error

#### BE-04.2: `backend/infrastructure/metrics.py`
- **Description**: Performance metrics collection
- **Inputs**: Metric names, values
- **Outputs**: Recorded metrics
- **Key Functions**:
  - `record_metric(name, value, tags)` → recorded metric
  - `start_timer(name)` → timer object
  - `end_timer(timer)` → elapsed time
  - `increment_counter(name)` → incremented counter
  - `get_metrics_report()` → metrics report

#### BE-04.3: `backend/infrastructure/task_queue.py`
- **Description**: Background task processing
- **Inputs**: Task functions, parameters
- **Outputs**: Task execution results
- **Key Functions**:
  - `enqueue_task(func, *args, **kwargs)` → task ID
  - `run_worker()` → worker process
  - `get_task_status(task_id)` → task status
  - `cancel_task(task_id)` → boolean success

#### BE-04.4: `backend/infrastructure/security.py`
- **Description**: Security utilities
- **Inputs**: Authentication data, API keys
- **Outputs**: Security validation results
- **Key Functions**:
  - `validate_api_key(api_key)` → validation result
  - `generate_api_key(user_id)` → new API key
  - `hash_password(password)` → hashed password
  - `verify_password(password, hash)` → boolean match

## Database Models (DB)

### DB-01: Graph Models
#### DB-01.1: `backend/models/graph.py`
- **Description**: Graph domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `name`: String graph name
  - `description`: Text description
  - `created_at`: DateTime creation timestamp
  - `updated_at`: DateTime update timestamp
  - `layout_data`: JSON layout information
  - `nodes`: One-to-many relationship to Node
  - `metadata`: JSON arbitrary metadata

#### DB-01.2: `backend/models/node.py`
- **Description**: Node domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `graph_id`: UUID foreign key to Graph
  - `name`: String node name
  - `node_type`: String node type identifier
  - `position_x`: Float X coordinate
  - `position_y`: Float Y coordinate
  - `properties`: JSON node configuration properties
  - `created_at`: DateTime creation timestamp
  - `updated_at`: DateTime update timestamp
  - `metadata`: JSON arbitrary metadata

#### DB-01.3: `backend/models/edge.py`
- **Description**: Edge domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `source_id`: UUID foreign key to source Node
  - `target_id`: UUID foreign key to target Node
  - `edge_type`: String edge type identifier
  - `created_at`: DateTime creation timestamp
  - `metadata`: JSON arbitrary metadata

### DB-02: Conversation Models
#### DB-02.1: `backend/models/conversation.py`
- **Description**: Conversation domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `node_id`: UUID foreign key to Node
  - `title`: String conversation title
  - `created_at`: DateTime creation timestamp
  - `updated_at`: DateTime update timestamp
  - `messages`: One-to-many relationship to Message
  - `metadata`: JSON arbitrary metadata

#### DB-02.2: `backend/models/message.py`
- **Description**: Message domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `conversation_id`: UUID foreign key to Conversation
  - `role`: String message role (user/assistant/system)
  - `content`: Text message content
  - `created_at`: DateTime creation timestamp
  - `metadata`: JSON arbitrary metadata

#### DB-02.3: `backend/models/context.py`
- **Description**: Context domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `conversation_id`: UUID foreign key to Conversation
  - `source_type`: String source type identifier
  - `source_id`: UUID source identifier
  - `content`: JSON context content
  - `created_at`: DateTime creation timestamp

### DB-03: Execution Models
#### DB-03.1: `backend/models/execution.py`
- **Description**: Execution domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `graph_id`: UUID foreign key to Graph
  - `status`: String execution status
  - `started_at`: DateTime start timestamp
  - `completed_at`: DateTime completion timestamp
  - `results`: One-to-many relationship to ExecutionResult
  - `metadata`: JSON execution metadata

#### DB-03.2: `backend/models/execution_result.py`
- **Description**: Execution result domain and ORM model
- **Key Fields**:
  - `id`: UUID primary key
  - `execution_id`: UUID foreign key to Execution
  - `node_id`: UUID foreign key to Node
  - `result`: JSON result data
  - `error`: JSON error information (if any)
  - `started_at`: DateTime start timestamp
  - `completed_at`: DateTime completion timestamp
  - `execution_time_ms`: Integer execution time in milliseconds

## External Integrations (EI)

### EI-01: AI Service Adapters
#### EI-01.1: `backend/integrations/ollama_client.py`
- **Description**: Ollama API client
- **Inputs**: API requests, model parameters
- **Outputs**: Ollama API responses
- **Key Functions**:
  - `list_models()` → available models list
  - `chat_completion(model, messages, params)` → completion response
  - `stream_chat_completion(model, messages, params)` → streamed response
  - `health_check()` → health status

#### EI-01.2: `backend/integrations/groq_client.py`
- **Description**: Groq API client
- **Inputs**: API requests, model parameters
- **Outputs**: Groq API responses
- **Key Functions**:
  - `list_models()` → available models list
  - `chat_completion(model, messages, params)` → completion response
  - `stream_chat_completion(model, messages, params)` → streamed response
  - `manage_rate_limits()` → rate limit manager

### EI-02: Plugin Architecture
#### EI-02.1: `backend/plugins/plugin_manager.py`
- **Description**: Plugin system manager
- **Inputs**: Plugin modules, configuration
- **Outputs**: Loaded plugins, extension points
- **Key Functions**:
  - `register_plugin(plugin_module)` → registered plugin
  - `get_plugins_for_hook(hook_name)` → plugins list
  - `call_hook(hook_name, *args, **kwargs)` → hook results
  - `load_plugins_from_directory(directory)` → loaded plugins

#### EI-02.2: `backend/plugins/node_extensions.py`
- **Description**: Custom node type extensions
- **Inputs**: Node data, execution context
- **Outputs**: Processing results
- **Key Functions**:
  - `register_node_type(type_name, handler)` → registered node type
  - `get_node_types()` → node types list
  - `process_node(node, context)` → processing result

#### EI-02.3: `backend/plugins/model_providers.py`
- **Description**: AI model provider extensions
- **Inputs**: Provider configuration, requests
- **Outputs**: Provider integration, responses
- **Key Functions**:
  - `register_provider(provider_name, client)` → registered provider
  - `get_providers()` → providers list
  - `get_provider(name)` → provider client
  - `list_all_models()` → all available models list

### EI-03: External API Support
#### EI-03.1: `backend/integrations/api_adapter.py`
- **Description**: Generic API adapter pattern
- **Inputs**: API configuration, requests
- **Outputs**: Standardized API responses
- **Key Functions**:
  - `create_client(api_config)` → API client
  - `execute_request(client, method, endpoint, data)` → request result
  - `handle_response(response)` → processed response
  - `handle_error(error)` → standardized error

#### EI-03.2: `backend/integrations/api_key_manager.py`
- **Description**: API key management
- **Inputs**: Service names, API keys
- **Outputs**: Secure API key access
- **Key Functions**:
  - `store_api_key(service_name, api_key)` → boolean success
  - `get_api_key(service_name)` → secured API key
  - `rotate_api_key(service_name, new_key)` → boolean success
  - `validate_api_key(service_name, key)` → validation result

This comprehensive file structure provides a detailed blueprint for implementing the AI Canvas architecture, with clear inputs, outputs, and responsibilities for each component.
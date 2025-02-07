
import pJITAI

# Create a new session to an existing API service
# session = pJITAI.Client(server='http://localhost/api', service_id='028fa04c-943d-4ae3-9885-55b4bdf4337e',
session = pJITAI.Client(server='http://localhost:85/api', service_id='8c1448a2-d8dd-41d8-b41c-63dda06e5ee0', service_token='e6e74d36-a3e4-4631-b077-4fdd703636f2')
service_token='e6e74d36-a3e4-4631-b077-4fdd703636f2'

# Upload some data
data = {
    'decision_id': 1,
    'decision_timestamp': '2022-06-01T08:30:00-05:00',
    'proximal_outcome': 45,
    'proximal_outcome_timestamp': '2022-06-01T09:00:00-05:00',
    'timestamp': '2022-06-01T09:05:00-05:00',
    'user_id': 'user_0',
    'values': [{
        'name': 'step_count',
        'value': 229
    }],
}
try:
    data_to_upload = pJITAI.DataVector.from_dict(data)
    # session.upload(data_to_upload)
    session.upload(data_to_upload, session.model['configuration']['eligibility'])
    print(data_to_upload)
except Exception as e:
    print(f'Upload Exception: {e}')

# Ask the server to generated a decision
data = {
    'timestamp': '2022-06-01T08:30:00-05:00',
    'user_id': 'user_0',
    'values': [{
        'name': 'step_count',
        'value': 24
    }]
}
try:
    decision = pJITAI.DecisionVector.from_dict(data)
    # session.decision(decision)
    session.decision(decision, session.model['configuration']['eligibility'])
    print(decision)
except Exception as e:
    print(f'Decision Exception: {e}')

# Have the server update the model parameters based on already uploaded data
try:
    session.update()
except Exception as e:
    print(f'Update Exception: {e}')
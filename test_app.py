import pytest
from jinja2 import DictLoader
from app import app as flask_app, workouts

# Provide an in-memory template so tests don't need a real file on disk
TEMPLATE = """
<!doctype html>
<html>
  <body>
    <ul id="workouts">
      {% for w in workouts %}
        <li class="workout">{{ w.workout }}: {{ w.duration }}</li>
      {% endfor %}
    </ul>
    <span id="count">{{ workouts|length }}</span>
  </body>
</html>
"""

@pytest.fixture(autouse=True)
def _setup_app_and_reset_workouts():
    # Use testing mode and inject a template
    flask_app.config.update(TESTING=True)
    flask_app.jinja_loader = DictLoader({"index.html": TEMPLATE})

    # Clear global state before each test
    workouts.clear()
    yield
    workouts.clear()

@pytest.fixture()
def client():
    with flask_app.test_client() as c:
        yield c

def test_home_renders_empty_list(client):
    resp = client.get("/")
    assert resp.status_code == 200
    html = resp.get_data(as_text=True)
    assert '<span id="count">0</span>' in html
    # No list items yet
    assert 'class="workout"' not in html
"""
def test_add_workout_success_redirects_and_persists(client):
    resp = client.post("/add", data={"workout": "Running", "duration": "30"})
    # Should redirect to home
    assert resp.status_code in (301, 302)
    # Follow the redirect and check the rendered list
    resp2 = client.get("/", follow_redirects=True)
    assert resp2.status_code == 200
    html = resp2.get_data(as_text=True)
    assert '<span id="count">1</span>' in html
    assert "Running: 30" in html
"""
def test_add_workout_missing_workout_returns_400(client):
    resp = client.post("/add", data={"duration": "20"})
    assert resp.status_code == 400
    assert b"Please enter both workout and duration." in resp.data

def test_add_workout_missing_duration_returns_400(client):
    resp = client.post("/add", data={"workout": "Cycling"})
    assert resp.status_code == 400
    assert b"Please enter both workout and duration." in resp.data

def test_add_workout_non_numeric_duration_returns_400(client):
    resp = client.post("/add", data={"workout": "Yoga", "duration": "abc"})
    assert resp.status_code == 400
    assert b"Duration must be a number." in resp.data
"""
def test_multiple_workouts_accumulate(client):
    client.post("/add", data={"workout": "Run", "duration": "25"})
    client.post("/add", data={"workout": "Swim", "duration": "40"})

    resp = client.get("/")
    assert resp.status_code == 200
    html = resp.get_data(as_text=True)
    # Expect two items
    assert '<span id="count">2</span>' in html
    assert "Run: 25" in html
    assert "Swim: 40" in html
    """
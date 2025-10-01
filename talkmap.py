"""
Leaflet cluster map of talk locations

Safe to run in CI: if dependencies or the `_talks` directory are missing,
the script exits successfully without side effects.
"""

import os
import sys
import glob

# Try optional dependencies; if missing (e.g., on CI), exit 0 gracefully
try:
    import frontmatter
except Exception:
    print("Skipping talkmap: 'python-frontmatter' not installed.")
    sys.exit(0)

try:
    from geopy import Nominatim
    from geopy.exc import GeocoderTimedOut
except Exception:
    print("Skipping talkmap: 'geopy' not installed.")
    sys.exit(0)

try:
    import getorg
except Exception:
    print("Skipping talkmap: 'getorg' not installed.")
    sys.exit(0)

# Set the default timeout, in seconds
TIMEOUT = 5

# Ensure talks directory exists
if not os.path.isdir("_talks"):
    print("Skipping talkmap: '_talks' directory not found.")
    sys.exit(0)

# Collect the Markdown files (if none, exit quietly)
g = glob.glob("_talks/*.md")
if not g:
    print("Skipping talkmap: no talk markdown files found.")
    sys.exit(0)

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    description = f"{title}<br />{venue}; {location}"

    # Geocode the location and report the status
    try:
        location_dict[description] = geocoder.geocode(location, timeout=TIMEOUT)
        print(description, location_dict[description])
    except ValueError as ex:
        print(f"Error: geocode failed on input {location} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {location} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {location} with message {ex}")

# Save the map only if we have at least one geocoded location
if not location_dict:
    print("Skipping talkmap: no geocoded locations.")
    sys.exit(0)

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)

# Track
An all-in-one python "module" that allows the user to get location data based on IP address and to interact/pull data from a host. The main module used
would be the IP2GeoTools module.

_TBH, I pulled this idea out of thin air and since I had the system, i turned that idea into code_

# Usage

```
python3 track.py -H <HOST_IP> [OPTIONS]
```

- Example:
```
python3 track.py -H 192.168.42.30 -C -c -L -l
```
- This will print out the: City, County, Latitude, and Longitude of the IP address.
- 

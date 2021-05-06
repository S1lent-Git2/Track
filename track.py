import argparse
from argparse import ArgumentParser as AG


def main():
    parse = AG(usage="python3 track.py -H <HOST_IP> [OPTION] | -h, --help", conflict_handler="resolve")
    parse.add_argument('-H', '--host', type=str, dest="track_host", metavar="", required=True, help="Set the host to \"probe\".")
    parse.add_argument('-V', '--version', action="store_true", dest="track_version", help="Display module version and exit.")
    parse.add_argument('--add-hosts', type=str, dest="track_add_hosts", metavar="", help="Add hosts to this session (temp).")
    parse.add_argument('--add-ports', type=str, dest="track_add_ports", metavar="", help="Add ports to this session (temp).")

    ## Location Data Grabbing section
    o1 = parse.add_argument_group("Location Grabbing Section", "Grabs location data such as City, County, Latitude and more.")
    o1.add_argument('-C', '--city', action="store_true", dest="track_city", help="Get the IP residual city name.")
    o1.add_argument('-R', '--region', action="store_true", dest="track_region", help="Get the IP residual region.")
    o1.add_argument('-c', '--country', action="store_true", dest="track_country", help="Get the IP residual country.")
    o1.add_argument('-L', '--latitude', action="store_true", dest="track_lat", help="Get IP's latitude position.")
    o1.add_argument('-l', '--longitude', action="store_true", dest="track_lon", help="Get IP's longitude position.")

    args = parse.parse_args()

    if args.track_host != "" or args.track_host:
        pass

    else:
        print("\n\033[37mPlease give me a host to probe...\033[0m\n"); exit(1)

if __name__ == '__main__':
    main()

from ubuntu:18.04

run apt-get -qq update && apt-get -qq --no-install-recommends install debconf
run echo "tzdata	tzdata/Areas	select	America" | debconf-set-selections
run echo "tzdata	tzdata/Zones/America	select	Los_Angeles" | debconf-set-selections
run DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get install -qq --no-install-recommends xinetd sagemath

run apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -qq --no-install-recommends xinetd sagemath

run apt-get install -qq git python-pip python-dev build-essential
#run git clone https://github.com/arthaud/python3-pwntools
#run sage -python3 -m pip install /python3-pwntools
run sage -python2 -m pip install pwntools

env PWNLIB_NOTERM true

COPY exploit.sage /

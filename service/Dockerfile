from ubuntu:18.04

run apt-get -qq update && apt-get -qq --no-install-recommends install debconf
run echo "tzdata	tzdata/Areas	select	America" | debconf-set-selections
run echo "tzdata	tzdata/Zones/America	select	Los_Angeles" | debconf-set-selections
run DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get install -qq --no-install-recommends xinetd sagemath

RUN mkdir -m a=wrx service_dir
copy service /service_dir/service
copy src/threshold.py /service_dir/threshold.py

# the deployment tester will pass in the flag from the yaml
ARG THE_FLAG="OOO{be_Smarter_like_you_just_did}"
RUN touch /flag && chmod 644 /flag && echo $THE_FLAG > /flag

copy service.conf /service.conf
copy banner_fail /banner_fail
copy banner /banner
copy wrapper /wrapper

expose 5000
cmd ["/usr/sbin/xinetd", "-syslog", "local0", "-dontfork", "-f", "/service.conf"]
# ^^ If ps would be too revealing, replace with the line below.
#    AFAIK, this also disables the built-in printf(%n) protection, so YMMV.
#cmd chmod go-rwx /proc && /usr/sbin/xinetd -syslog local0 -dontfork -f /service.conf

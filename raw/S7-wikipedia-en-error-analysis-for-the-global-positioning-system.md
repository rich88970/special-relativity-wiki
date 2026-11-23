---
id: S7
title: Error analysis for the Global Positioning System
source: Wikipedia（en）
url: https://en.wikipedia.org/wiki/Error_analysis_for_the_Global_Positioning_System
revision: 1377400056（2026-09-29T05:31:20Z）
license: CC BY-SA 4.0（原文作者為維基百科貢獻者）
fetched: 2026-11-23
note: 以 MediaWiki API 取得純文字，原樣保存，匯入後不修改
---

The error analysis for the Global Positioning System is important for understanding how GPS works, and for knowing what magnitude of error should be expected. The GPS makes corrections for receiver clock errors and other effects but there are still residual errors which are not corrected. GPS receiver position is computed based on data received from the satellites. Errors depend on geometric dilution of precision and the sources listed in the table below.


== Overview ==

User equivalent range errors (UERE) are shown in the table. There is also a numerical error with an estimated value,  σnum, of about 1 meter (3 ft 3 in). The standard deviations,  σR, for the coarse/acquisition (C/A) and precise codes are also shown in the table. These standard deviations are computed by taking the square root of the sum of the squares of the individual components (i.e., RSS for root sum squares). To get the standard deviation of receiver position estimate, these range errors must be multiplied by the appropriate dilution of precision terms and then RSS'ed with the numerical error. Electronics errors are one of several accuracy-degrading effects outlined in the table above. When taken together, autonomous civilian GPS horizontal position fixes are typically accurate to about 15 meters (50 ft). These effects also reduce the more precise P(Y) code's accuracy. However, the advancement of technology means that in the present, civilian GPS fixes under a clear view of the sky are on average accurate to about 5 meters (16 ft) horizontally.
The term user equivalent range error (UERE) refers to the error of a component in the distance from receiver to a satellite. These UERE errors are given as ± errors thereby implying that they are unbiased or zero mean errors. These UERE errors are therefore used in computing standard deviations. The standard deviation of the error in receiver position,
 σrc, is computed by multiplying PDOP (Position Dilution Of Precision) by
 σR, the standard deviation of the user equivalent range errors.
 σR is computed by taking the square root of the sum of the squares of the individual component standard deviations.
PDOP is computed as a function of receiver and satellite positions. A detailed description of how to calculate PDOP is given in the section Geometric dilution of precision computation (GDOP).
 σR for the C/A code is given by:

3σR=32+52+2.52+22+12+0.52m=6.7m
The standard deviation of the error in estimated receiver position  σrc, again for the C/A code is given by:

 σrc=PDOP2×σR2+σnum2=PDOP2×2.22+12m
The error diagram on the left shows the inter relationship of indicated receiver position, true receiver position, and the intersection of the four sphere surfaces.


== Signal arrival time measurement ==
The position calculated by a GPS receiver requires the current time, the position of the satellite and the measured delay of the received signal. The position accuracy is primarily dependent on the satellite position and signal delay.
To measure the delay, the receiver compares the bit sequence received from the satellite with an internally generated version. By comparing the rising and trailing edges of the bit transitions, modern electronics can measure signal offset to within about one percent of a bit pulse width, 0.01×300,000,000 m/s(1.023×106/s), or approximately 10 nanoseconds for the C/A code. Since GPS signals propagate at the speed of light, this represents an error of about 3 meters.
This component of position accuracy can be improved by a factor of 10 using the higher-chirprate P(Y) signal. Assuming the same one percent of bit pulse width accuracy, the high-frequency P(Y) signal results in an accuracy of (0.01×300,000,000 m/s)(10.23×106/s) or about 30 centimeters. The civilian L5 signal features the same increase in chirp rate.


=== Carrier phase measurement ===

More advanced GPS receivers measures of the phase of the signal's carrier wave in addition to the standard code phase measurement. Because the carriers are at a higher frequency (1.18–1.58 GHz), performing phase measurements on this signal would yield a 0.2 cm error using the same assumption of 1% phase error. The receiver needs to have a way to resolve the pseudorange ambiguity from the phase resetting every 19 cm. This is possible by comparing the phases of multiple satellites or with the help of a ground station with known location.


== Atmospheric effects ==
Inconsistencies of atmospheric conditions affect the speed of the GPS signals as they pass through the Earth's atmosphere, especially the ionosphere. Correcting these errors is a significant challenge to improving GPS position accuracy. These effects are smallest when the satellite is directly overhead and become greater for satellites nearer the horizon since the path through the atmosphere is longer (see airmass). Once the receiver's approximate location is known, a mathematical model can be used to estimate and compensate for these errors.


=== Ionospheric delay ===
Ionospheric delay of a microwave signal depends on its frequency. It arises from ionized atmosphere (see Total electron content). This phenomenon is known as dispersion and can be calculated from measurements of delays for two or more frequency bands, allowing delays at other frequencies to be estimated. Some military and expensive survey-grade civilian receivers calculate atmospheric dispersion from the different delays in the L1 and L2 frequencies, and apply a more precise correction. This can be done in civilian receivers without decrypting the P(Y) signal carried on L2, by tracking the carrier wave instead of the modulated code. To facilitate this on lower cost receivers, a new civilian code signal on L2, called L2C, was added to the Block IIR-M satellites, which was first launched in 2005. It allows a direct comparison of the L1 and L2 signals using the coded signal instead of the carrier wave.
The effects of the ionosphere generally change slowly, and can be averaged over time. Those for any particular geographical area can be easily calculated by comparing the GPS-measured position to a known surveyed location. This correction is also valid for other receivers in the same general location. Several systems send this information over radio or other links to allow L1-only receivers to make ionospheric corrections. The ionospheric data are transmitted via satellite in Satellite Based Augmentation Systems (SBAS) such as Wide Area Augmentation System (WAAS) (available in North America and Hawaii), EGNOS (Europe and Asia), Multi-functional Satellite Augmentation System (MSAS) (Japan), and GPS Aided Geo Augmented Navigation (GAGAN) (India) which transmits it on the GPS frequency using a special pseudorandom noise sequence (PRN), so only one receiver and antenna are required.


=== Weather conditions ===
Humidity also causes a variable delay, resulting in errors similar to ionospheric delay, but occurring in the troposphere. This effect is more localized than ionospheric effects, changes more quickly and is not frequency dependent. These traits make precise measurement and compensation of humidity errors more difficult than ionospheric effects.
The Atmospheric pressure can also change the signals reception delay, due to the dry gases present at the troposphere (78% N2, 21% O2, 0.9% Ar...). Its effect varies with local temperature and atmospheric pressure in quite a predictable manner using the laws of the ideal gases.


== Multipath effects ==
GPS signals can also be affected by multipath issues, where the radio signals reflect off surrounding terrain; buildings, canyon walls, hard ground, etc. These delayed signals cause measurement errors that are different for each type of GPS signal due to its dependency on the wavelength.
A variety of techniques, most notably narrow correlator spacing, have been developed to mitigate multipath errors. For long delay multipath, the receiver itself can recognize the wayward signal and discard it. To address shorter delay multipath from the signal reflecting off the ground, specialized antennas (e.g., a choke ring antenna) may be used to reduce the signal power as received by the antenna. Short delay reflections are harder to filter out because they interfere with the true signal, causing effects almost indistinguishable from routine fluctuations in atmospheric delay.
Multipath errors are more severe in "urban canyons" where buildings block the view of a satellite, leaving the reflected signal as the only observation of the satellite. Choke ring antennas are also less applicable because signals may bounce off of other buildings (therefore appearing as "from above"). The net result is that when a user stands on the eastern side of a street with the eastern half of view of the sky blocked, multipath effects tend to result in an apparent location that is moved westwards. Uber has deployed an ambiguity resolution method using measured SNR values to "shadow-match" against predicted SNR values around the apparent location, an extension of a method originally developed by Paul Groves.
Multipath effects are much less severe in moving vehicles. When the GPS antenna is moving, the false solutions using reflected signals quickly fail to converge and only the direct signals result in stable solutions.


== Ephemeris and clock errors ==
While the ephemeris data is transmitted every 30 seconds, the information itself may be up to two hours old. Variability in solar radiation pressure has an indirect effect on GPS accuracy due to its effect on ephemeris errors. If a fast time to first fix (TTFF) is needed, it is possible to upload a valid ephemeris to a receiver, and in addition to setting the time, a position fix can be obtained in under ten seconds. It is feasible to put such ephemeris data on the web so it can be loaded into mobile GPS devices. See also Assisted GPS.
The satellites' atomic clocks experience noise and clock drift errors. The navigation message contains corrections for these errors and estimates of the accuracy of the atomic clock. However, they are based on observations and may not indicate the clock's current state.
These problems tend to be very small, but may add up to a few meters (tens of feet) of inaccuracy.
For very precise positioning (e.g., in geodesy), these effects can be eliminated by differential GPS: the simultaneous use of two or more receivers at several survey points. In the 1990s when receivers were quite expensive, some methods of quasi-differential GPS were developed, using only one receiver but reoccupation of measuring points. At the TU Vienna the method was named qGPS and post processing software was developed.
The International GNSS Service (IGS) uses its global network of monitoring stations to produce higher-accuracy ephemerides and clock drift data for the GPS satellites. The IGS produces and archives the coarse estimates broadcast by the satellites, a finer ultra-rapid observation and prediction published four times per day, an even finer "rapid" data from daily post-processing, and the finest "final" data published weekly. The ultra-rapid prediction can be used in real time to refine results. The other data can be used on recorded GPS data to produce high-accuracy results after the fact.


== Dilution of precision ==

Dilution of precision describes the effect of satellite geometry on how pseudorange errors propagate into positioning and velocity error.


== Selective Availability ==
GPS formerly included a feature called Selective Availability (SA) that added intentional, time varying errors of up to 100 meters (328 ft) to the publicly available navigation signals. This was intended to deny an enemy the use of civilian GPS receivers for precision weapon guidance.
SA errors are actually pseudorandom, generated by a cryptographic algorithm from a classified seed key available only to authorized users (the U.S. military, its allies and a few other users, mostly government) with a special military GPS receiver. Mere possession of the receiver is insufficient; it still needs the tightly controlled daily key.
Before it was turned off on May 2, 2000, typical SA errors were about 50 m (164 ft) horizontally and about 100 m (328 ft) vertically. Because SA affects every GPS receiver in a given area almost equally, a fixed station with an accurately known position can measure the SA error values and transmit them to the local GPS receivers so they may correct their position fixes. This is called Differential GPS (DGPS). DGPS also corrects for several other important sources of GPS errors, particularly ionospheric delay, so it continues to be widely used even though SA has been turned off. The ineffectiveness of SA in the face of widely available DGPS was a common argument for turning off SA, and this was finally done by order of President Clinton in 2000.
DGPS services are widely available from both commercial and government sources. The latter include WAAS and the U.S. Coast Guard's network of LF marine navigation beacons. The accuracy of the corrections depends on the distance between the user and the DGPS receiver. As the distance increases, the errors at the two sites will not correlate as well, resulting in less precise differential corrections.
During the 1990–91 Gulf War, the shortage of military GPS units caused many troops and their families to buy readily available civilian units. Selective Availability significantly impeded the U.S. military's own battlefield use of these GPS, so the military made the decision to turn it off for the duration of the war.
In the 1990s, the FAA started pressuring the military to turn off SA permanently. This would save the FAA millions of dollars every year in maintenance of their own radio navigation systems. The amount of error added was "set to zero" at midnight on May 1, 2000 following an announcement by U.S. President Bill Clinton, allowing users access to the error-free L1 signal. Per the directive, the induced error of SA was changed to add no error to the public signals (C/A code). Clinton's executive order required SA to be set to zero by 2006; it happened in 2000 once the U.S. military developed a new system that provides the ability to deny GPS (and other navigation services) to hostile forces in a specific area of crisis without affecting the rest of the world or its own military systems.
On 19 September 2007, the United States Department of Defense announced that future GPS III satellites will not be capable of implementing SA, eventually making the policy permanent.


== Anti-spoofing ==

Another restriction on GPS, antispoofing, remains on. This encrypts the P-code so that it cannot be mimicked by a transmitter sending false information. Few civilian receivers have ever used the P-code, and the accuracy attainable with the public C/A code was much better than originally expected (especially with DGPS), so much so that the antispoof policy has relatively little effect on most civilian users. Turning off antispoof would primarily benefit surveyors and some scientists who need extremely precise positions for experiments such as tracking tectonic plate motion.


== Relativity ==
The theory of relativity introduces several effects that need to be taken into account when dealing with precise time measurements. According to special relativity, time passes differently for objects in relative motion. That is known as kinetic time dilation: in an inertial reference frame, the faster an object moves, the slower its time appears to pass
(as measured by the frame's clocks). General relativity takes into account also the effects that gravity has on the passage of time. In the context of GPS the most prominent correction introduced by general relativity is gravitational time dilation: the clocks located deeper in the gravitational potential well (i.e. closer to the attracting body) tick slower.


=== Special relativity ===
Special relativity predicts that as the velocity of an object increases (in a given frame), its time slows down (as measured in that frame). For instance, the frequency of the atomic clocks moving at GPS orbital speeds will tick more slowly than stationary clocks by a factor of v2/2c2≈10−10 where the orbital velocity is v = 4 km/s and c is the speed of light, approximately 3×108m/s.  The result is an error of about -7.2 μs/day in the satellite. The special relativistic effect is due to the constant movement of GPS clocks relative to the Earth-centered, non-rotating approximately inertial reference frame.  In short, the clocks on the satellites are slowed down by the velocity of the satellite. This time dilation effect has been measured and verified using the GPS.


=== General relativity ===
Special relativity allows the comparison of clocks only in a flat spacetime, which neglects gravitational effects on the passage of time. According to general relativity, the presence of gravitating bodies (like Earth) curves spacetime, which makes comparing clocks not as straightforward as in special relativity. However, one can often account for most of the discrepancy by the introduction of gravitational time dilation, the slowing down of time near gravitating bodies. In case of the GPS, the receivers are closer to the center of Earth than the satellites, causing the clocks at the altitude of the satellite to be faster by a factor of 5×10−10, or about +45.8 μs/day. This gravitational frequency shift is measurable.  During early development some believed that GPS would not be affected by general relativistic effects, but the Hafele–Keating experiment showed that it would be.


=== Combined kinetic and gravitational time dilations ===
Combined, these sources of time dilation cause the clocks on the satellites to gain 38.6 microseconds per day relative to the clocks on the ground. This is a difference of 4.465 parts in 1010. Without correction, errors of roughly 11.4 km/day would accumulate in the position. This initial pseudorange error is corrected in the process of solving the navigation equations. In addition, the elliptical, rather than perfectly circular, satellite orbits cause the time dilation and gravitational frequency shift effects to vary with time. This eccentricity effect causes the clock rate difference between a GPS satellite and a receiver to increase or decrease depending on the altitude of the satellite.
To compensate for the discrepancy, the frequency standard on board each satellite is given a rate offset prior to launch, making it run slightly slower than the desired frequency on Earth; specifically, at 10.22999999543 MHz instead of 10.23 MHz. Since the atomic clocks on board the GPS satellites are precisely tuned, it makes the system a practical engineering application of the scientific theory of relativity in a real-world environment. Placing atomic clocks on artificial satellites to test Einstein's general theory was proposed by Friedwardt Winterberg in 1955.


=== Calculations ===
To calculate the amount of daily time dilation experienced by GPS satellites relative to Earth we need to separately determine the amounts due to the satellite's velocity and altitude, and add them together.


==== Kinetic time dilation ====
The amount due to velocity is determined using the Lorentz transformation. The time measured by an object moving with velocity v changes by (the inverse of) the Lorentz factor:

1γ=1−v2c2
For small values of v/c this approximates to:

1γ≈1−v22c2
The GPS satellites move at 3874 m/s relative to Earth's center. We thus determine:

1γ≈1−387422(2.998×108)2≈1−8.349×10−11
This difference of 8.349×10−11 represents the fraction by which the satellites' clocks tick slower than the stationary clocks. It is then multiplied by the number of nanoseconds in a day:

−8.349×10−11×60×60×24×109≈−7214 ns
That is, the satellites' clocks are slower than Earth's clocks by 7214 nanoseconds a day due to their velocity.

Note that this speed of 3874 m/s is measured relative to Earth's center rather than its surface where the GPS receivers (and users) are. This is because Earth's equipotential makes net time dilation equal across its geodesic surface. That is, the combination of Special and General effects make the net time dilation at the equator equal to that of the poles, which in turn are at rest relative to the center. Hence we use the center as a reference point to represent the entire surface.


==== Gravitational time dilation ====
The amount of dilation due to gravity is determined using the gravitational time dilation equation:

trt∞=1−2GMrc2
where tr is the time passed at a distance r from the center of the Earth and t∞ is the time passed for a far away observer.
For small values of GM/(rc2) this approximates to:

trt∞≈1−GMrc2
Determine the difference Δt between the satellite's time trGPS and Earth time trEarth:

Δt≈(1−GMrGPSc2)−(1−GMrEarthc2)=GMrEarthc2−GMrGPSc2
Earth has a radius of 6,357 km (at the poles) making rEarth = 6,357,000 m and the satellites have an altitude of 20,184 km making their orbit radius rGPS  = 26,541,000 m. Substituting these in the above equation, with Earth mass M = 5.974×1024, G = 6.674×10−11, and c = 2.998×108 (all in SI units), gives:

Δt≈5.307×10−10
This represents the fraction by which the clocks at satellites' altitude tick faster than on the surface of the Earth. It is then multiplied by the number of nanoseconds in a day:

5.307×10−10×60×60×24×109≈45850 ns
That is, the satellites' clocks gain 45850 nanoseconds a day due to gravitational time dilation.


==== Combined time dilation effects ====
These effects are added together to give (rounded to 10 ns):

45850 – 7210 = 38640 ns
Hence the satellites' clocks gain approximately 38,640 nanoseconds a day or 38.6 μs per day due to relativistic effects in total.
In order to compensate for this gain, a GPS clock's frequency needs to be slowed by the fraction:

5.307×10−10 –  8.349×10−11 = 4.472×10−10
This fraction is subtracted from 1 and multiplied by the pre-adjusted clock frequency of 10.23 MHz:

(1 –  4.472×10−10) × 10.23 = 10.22999999543
That is, we need to slow the clocks down from 10.23 MHz to 10.22999999543 MHz in order to negate both time dilation effects.


=== Sagnac distortion ===
GPS observation processing must also compensate for the Sagnac effect. The GPS time scale is defined in an inertial system but observations are processed in an Earth-centered, Earth-fixed (co-rotating) system. A coordinate transformation is thus applied to convert from the inertial system to the ECEF system. The resulting signal run time correction has opposite algebraic signs for satellites in the Eastern and Western celestial hemispheres. Ignoring this effect will produce an east–west error on the order of hundreds of nanoseconds, or tens of meters in position.


== Natural sources of interference ==
Since GPS signals at terrestrial receivers tend to be relatively weak, natural radio signals or scattering of the GPS signals can desensitize the receiver, making acquiring and tracking the satellite signals difficult or impossible.
Space weather degrades GPS operation in two ways, direct interference by solar radio burst noise in the same frequency band or by scattering of the GPS radio signal in ionospheric irregularities referred to as scintillation. Both forms of degradation follow the 11 year solar cycle and are a maximum at sunspot maximum although they can occur at any time. Solar radio bursts are associated with solar flares and coronal mass ejections (CMEs) and their impact can affect reception over the half of the Earth facing the sun. Scintillation occurs most frequently at tropical latitudes where it is a night time phenomenon. It occurs less frequently at high latitudes or mid-latitudes where magnetic storms can lead to scintillation. In addition to producing scintillation, magnetic storms can produce strong ionospheric gradients that degrade the accuracy of SBAS systems.


== Artificial sources of interference ==
In automotive GPS receivers, metallic features in windshields, such as defrosters, or car window tinting films can act as a Faraday cage, degrading reception just inside the car.
Man-made EMI (electromagnetic interference) can also disrupt or jam GPS signals. In one well-documented case it was impossible to receive GPS signals in the entire harbor of Moss Landing, California due to unintentional jamming caused by malfunctioning TV antenna preamplifiers. Intentional jamming is also possible. Generally, stronger signals can interfere with GPS receivers when they are within radio range or line of sight. In 2002 a detailed description of how to build a short-range GPS L1 C/A jammer was published in the online magazine Phrack.
The U.S. government reported that such jammers were used occasionally during the War in Afghanistan, and the U.S. military destroyed six GPS jammers during the Iraq War, including one that was destroyed with a GPS-guided bomb, noting the ineffectiveness of the jammers used in that situation. A GPS jammer is relatively easy to detect and locate, making it an attractive target for anti-radiation missiles. The UK Ministry of Defence tested a jamming system in the UK's West Country on 7 and 8 June 2007.
Some countries allow the use of GPS repeaters to allow the reception of GPS signals indoors and in obscured locations; while in other countries these are prohibited as the retransmitted signals can cause multi-path interference to other GPS receivers that receive data from both GPS satellites and the repeater. In the UK Ofcom now permits the use of GPS/GNSS Repeaters under a 'light licensing' regime.
Due to the potential for both natural and man-made noise, numerous techniques continue to be developed to deal with the interference. The first is to not rely on GPS as a sole source. According to John Ruley, "IFR pilots should have a fallback plan in case of a GPS malfunction". Receiver Autonomous Integrity Monitoring (RAIM) is a feature included in some receivers, designed to provide a warning to the user if jamming or another problem is detected. The U.S. military has also deployed since 2004 their Selective Availability / Anti-Spoofing Module (SAASM) in the Defense Advanced GPS Receiver (DAGR). In demonstration videos the DAGR was shown to detect jamming and maintain its lock on the encrypted GPS signals during interference which caused civilian receivers to lose lock.


== See also ==
GNSS enhancement


== Notes ==


== References ==
Grewal, Mohinder S.; Weill, Lawrence Randolph; Andrews, Angus P. (2001). Global positioning systems, inertial navigation, and integration. John Wiley and Sons. ISBN 978-0-471-35032-3.
Parkinson; Spilker (1996). The global positioning system. American Institute of Aeronautics & Astronomy. ISBN 978-1-56347-106-3.
Webb, Stephen (2004). Out of this world: colliding universes, branes, strings, and other wild ideas of modern physics. Springer. ISBN 0-387-02930-3. Retrieved 2013-08-16.


== External links ==

GPS.gov—General public education website created by the U.S. Government
GPS SPS Performance Standard Archived 2017-04-27 at the Wayback Machine—The official Standard Positioning Service specification (2008 version).
GPS SPS Performance Standard—The official Standard Positioning Service specification (2001 version).

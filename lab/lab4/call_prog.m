vr = [];
iLine = [];
for s = 0:10:100
   [x z] = VR2(s,25,C_v,C_I)
   vr = [vr x];
   iLine = [iLine z];
end

S = 0:10:100;

figure
plot(S,vr)
title('S load magnitude versus % voltage regulation')
xlabel('S load magnitude (VA)')
ylabel('voltage regulation (%)')

figure
plot(S,iLine)
title('S load magnitude versus line current')
xlabel('S load magnitude (VA)')
ylabel('line current (A)')

vr = [];
iLine = [];
for p = -90:10:90
   [x z] = VR2(60,p,C_v,C_I)
   vr = [vr x];
   iLine = [iLine z];
end

P = -90:10:90;

figure
plot(P,vr)
title('S load phase versus % voltage regulation')
xlabel('S load phase (degrees)')
ylabel('voltage regulation (%)')

figure
plot(P,iLine)
title('S load phase versus line current')
xlabel('S load phase (degrees)')
ylabel('line current (A)')
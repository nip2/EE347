% program takes sLoad_mag, sLoad_phi (degrees), C_v, C_I
% C_v is a 2 element array of under and over voltage coefficients
% such that C_v(1)*V_p is the threshold of undervoltage
% returns voltage regulation as a percent

% These are default values:
% Overcurrent coeff
C_I = 1.1;
% under/over voltage coeffs
C_v = [0.95, 1.2];

% Function For Checking Overcurrent
function OverCurrentCheck = OverCurrentCheck(I_line, C_I, I_rated)
   if I_line > C_I * I_rated
       cFlag = 'Over-current Flag!';
   end
end

% Function For Checking Under-Overvoltage
function UnderOverVoltageCheck = UnderOverVoltageCheck(V_p,C_v)
   if V_p <= C_v(1)*V_p
       vFlag = 'Under-voltage Flag!';
   end
   if V_p >= C_v(2)*V_p
       vFlag = 'Over-voltage Flag!';
   end
end

% Function to find efficiency
function Efficiency = Efficiency(S_rated, sLoad_phi, iLine, Vp_fl)
   # resistance values found from lab testing
   Reqp = 17.24;
   Rcore = 6667;
   
   % find the power loss
   P_core = Vp_fl^2 / Rcore;
   P_cu = iLine^2*Reqp;
   PF = cos(deg2rad(sLoad_phi));
   %disp("PF:")
   %disp(PF)
   P_out = S_rated * PF;
   % calculate efficiency
   eff = P_out / (P_out + P_core + P_cu) * 100;
   %sprintf('Efficiency: %.2f %%', eff)
end

% Function to return voltage regulation
% also checks for overcurrent and over/under voltage
% also reports power transfer efficiency
function [vr iLine_mag] = VR2(sLoad_mag, sLoad_phi, C_v, C_I)
   S_rated = 60;
   I_rated = 0.5;
   V_s = 120;
   Reqp = 17.24;
   Xeqp = 23.73;
   inFlag = 'None';
   cFlag = 'None';
   vFlag = 'None';
   
   % check if input sLoad_mag is within range
   if sLoad_mag > 1.8 * S_rated
       inFlag = 'sLoad too high!';
   % check if input sLoad_phi is within range
   elseif sLoad_mag < 0
       inFlag = 'sLoad too low!'
   elseif sLoad_phi < -90 || sLoad_phi > 90
       inFlag = 'sLoad angle out of bounds!';
   % If the above are true, then perform calculations
   else
       % generate single complex S_load variable
       [sL_re,sL_im] = pol2cart(deg2rad(sLoad_phi),sLoad_mag);
       sL_conj = complex(sL_re,-sL_im);
       % find line current
       iLine = sL_conj / V_s;
       
       % check that the line current isn't over specified threshold
       iLine_mag = abs(iLine);
       OverCurrentCheck(iLine_mag, C_I, I_rated)
       
       % find full load primary voltage
       Vp_fl = abs(iLine^2 * complex(Reqp,Xeqp)) + V_s;
       
       % check that the primary voltage isn't under or over threshold
       UnderOverVoltageCheck(Vp_fl, C_v)
       
       % find the efficiency of power transform
       Efficiency(S_rated, sLoad_phi, iLine_mag, Vp_fl);
       
       % find the voltage regulation
       V_reg = abs(Vp_fl - V_s) / V_s * 100;
       %sprintf('Voltage regulation: %.1f %%', V_reg)
       vr = V_reg;
   end
   
end

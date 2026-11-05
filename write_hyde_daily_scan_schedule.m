
%%

% 000010	
line1='hyde_VAD_scan_1deg_2 1	S	6';
% 000100	
line2='hyde_VAD_scan_5deg	1	S	6';
% 000130
line3='VAD_scan_30deg	3	S	6';
% 000240
line4='VAD_scan_70deg	3	S	6';
% 000320	
% line5='S_12stare	10	S	6';


%%
fid=fopen('hyde_shedule_1.dss','w');

timen=0:15/(60*24):24;

for i=1:(length(timen)-1)
    hh=datestr(timen(i)+10/(24*60*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line1);
    hh=datestr(timen(i)+1/(24*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line2);
    hh=datestr(timen(i)+1.5/(24*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line3);
    hh=datestr(timen(i)+160/(24*60*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line4);
end
fclose(fid);

%%
%%

% 000010	
line1='hyde_VAD_scan_1deg_2 3	S	6';
% 000100	
line2='hyde_VAD_scan_5deg	3	S	6';
% 000130
line3='VAD_scan_30deg	3	S	6';
% 000240
line4='VAD_scan_70deg	3	S	6';
% 000320	
% line5='S_12stare	10	S	6';


%%
fid=fopen('hyde_shedule_2.dss','w');

timen=0:15/(60*24):24;

for i=1:(length(timen)-1)
    hh=datestr(timen(i)+10/(24*60*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line1);
    hh=datestr(timen(i)+160/(24*60*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line2);
    hh=datestr(timen(i)+240/(24*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line3);
    hh=datestr(timen(i)+310/(24*60*60),'HHMMSS');
    fprintf(fid,'%s\t%s\n',hh,line4);
end
fclose(fid);















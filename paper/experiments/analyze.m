% D:\Dropbox\Papers\Amy\encounternet>awk -f analyze.awk rfexperiment rfexperiment2 rfexperiment4 > rfexp_matlab.txt
%
%
%

function analyze()

    RAW = load('rfexp_matlab.txt','-ascii');
    size(RAW)

    % experiment one
    
    r = stats( 78  ,  0, timeToNum(09,55, 0), timeToNum(10,06, 0) );
    r = stats( 53  ,  0, timeToNum(10,13, 0), timeToNum(10,20, 0) );
    [r,mr(4),d(4)] = stats( 18.5,  0, timeToNum(10,25, 0), timeToNum(10,30, 0) );
    close all;
    figure
    ax=axes
    h1=histogram(ax,r)
    h1.Normalization = 'probability';
    h1.BinWidth = 1;
    r = stats( 18.5, 90, timeToNum(10,30,30), timeToNum(10,36, 0) );
    [r,mr(3),d(3)] = stats( 10.2,  0, timeToNum(10,37,30), timeToNum(10,44, 0) );
    hold on
    h2=histogram(ax,r)
    h2.Normalization = 'probability';
    h2.BinWidth = 1;
    [r,mr(2),d(2)] = stats(  5.2,  0, timeToNum(10,45, 0), timeToNum(10,50, 0) );
    h3=histogram(ax,r)
    h3.Normalization = 'probability';
    h3.BinWidth = 1;
    [r,mr(1),d(1)] = stats(  2.0,  0, timeToNum(10,51, 0), timeToNum(10,57, 0) );
    h3=histogram(ax,r)
    h3.Normalization = 'probability';
    h3.BinWidth = 1;
    r = stats( 78.0,  0, timeToNum(11,07, 0), timeToNum(11,12, 0) );
    r = stats( 78.0, 90, timeToNum(11,12, 0), timeToNum(11,18, 0) );
    r = stats( 10.2, 90, timeToNum(11,22,00), timeToNum(11,27, 0) );
    r = stats( 10.2,  0, timeToNum(11,27,20), timeToNum(11,33, 0) );
    set(gca,'FontName','Helvetica');
    h = legend('18.5 m','10.2 m',' 5.2 m','2.0 m', 'Location','NorthWest');
    set(h,'FontName','Helvetica');
    xlabel('RSSI (dB)');
    ylabel('fraction');
    print -depsc2 rssiHistograms.eps
    
    ratios = d./d(1);
    dBdiffs = 6*log2(ratios)
    mr'
    %A = [ ones(4,1) sqrt(ratios)' ];
    A = ones(4,1) ;
    model = A\(mr+dBdiffs)'
    A*model - dBdiffs'
    
    figure
    plot(d,mr,'ks-',d,A*model - dBdiffs','ro-');
    axis([0 20 -100 -65]);
    xlabel('distance (m)');
    ylabel('RSSI (dB)');
    set(gca,'FontName','Helvetica');
    print -depsc2 rssiDistance.eps
    drawnow
    
    function [rssi,mfrssi,d] = stats( distance, angle, t1, t2 )
        d = distance;
        rssi = [];
        mfrssi = NaN;
        ii = find( (RAW(:,1) >=t1) .* (RAW(:,1) <t2) .* (RAW(:,4)==0) );
        data = RAW( ii, : );
        %size(ii)
        %size(RAW)
        %size(data)
        ts = NaN;
        ns = NaN;
        te = NaN;
        ne = NaN;
        m = size(data,1);
        if m==0; 
            fprintf('%.1f %d %.0f missing data\n',distance, angle, t2-t1); 
            return; 
        end
        %for j=1:m
        %    %data(j,:)
        %    if isnan(ts)
        %        ts = data(j,1);
        %       ns = data(j,2);
        %        js = j;
        %        [ts ns]
        %    end
        %    te = data(j,1);
        %    ne = data(j,2);
        %    je = j;
        %end      
        ns = data(1,2);
        ts = data(1,1);
        ne = data(m,2);
        te = data(m,1);
        %
        %[ts te ns ne]
        
        ntotal = ne-ns+1;
        ngood  = m; % je-js+1;
        
        rxFraction = ngood/ntotal;
        txRate = ntotal/(te-ts);
        
        rssi = sort(data(:,3));
        mfrssi = mean( rssi( ceil(m/4):floor(3*m/4) ) );
        
        fprintf('%.1f %d %.0f %f %f %f %f %.0f\n',distance, angle, t2-t1, ntotal, ngood, rxFraction, txRate, mfrssi); 
    end


    function it = timeToNum(hours,minutes,seconds)
        it = 3600*hours + 60*minutes + seconds;
    end
end
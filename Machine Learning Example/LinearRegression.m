clc,clear all,close all,

length = 60;
a = rand(length,1); 
b = 100-(rand(length,1) + a * 5);
figure(1)
scatter(a,b)

%[length,~] = size(a);
a_mean = mean(a); b_mean = mean(b);

afactor = zeros(length,1);bfactor = zeros(length,1);
afactor2 = zeros(length,1);bfactor2 = zeros(length,1);
abfactor = zeros(length,1);
for i = 1:length
    % summation of each (a-mean(a)) 
    afactor(i) = a(i) - a_mean;
    afactor2(i) = (a(i) - a_mean)^2;
    % summation of each (b-mean(b)) 
    bfactor(i) = b(i) - b_mean;
    bfactor2(i) = (b(i) - b_mean)^2;
    abfactor(i) = (a(i) - a_mean) * (b(i) - b_mean);
end

a_cov = sum(afactor2)/length;
b_cov = sum(bfactor2)/length;
ab_cov = sum(abfactor)/length;

slope = ab_cov / a_cov;
interception = b_mean - slope * a_mean;

predict = slope * a + interception;

hold on;
plot(a,predict,'-r')

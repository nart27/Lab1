program KONG;

Uses DateUtils;

var
  x: longword = 10;
  m: longword;
 
procedure init();
begin
  m:=Round(exp(32*ln(2))-1);
end;
function rand():longword;
begin
  x:=(1664525*x+1013904223) mod m;
  rand:=x;
end;

procedure test();
  var i:integer;
begin
  for i:=1 to 10 do
  begin
	writeln('Rand value is ', rand());
  end;
end;

begin
  init();
  test();
end.

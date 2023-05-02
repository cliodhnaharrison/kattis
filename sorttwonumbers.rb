num = gets.chomp.split
if num[0].to_i > num[1].to_i
  puts "#{num[1]} #{num[0]}"
else
  puts "#{num[0]} #{num[1]}"
end

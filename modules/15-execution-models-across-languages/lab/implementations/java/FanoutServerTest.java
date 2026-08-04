public final class FanoutServerTest {
  public static void main(String[] args) throws Exception {
    if(FanoutServer.parse("{\"request_id\":\"x\",\"deadline_ms\":500,\"concurrency_limit\":4,\"children\":[]}")!=null)throw new AssertionError("empty children accepted");
    if(FanoutServer.parse("{\"request_id\":\"x\",\"deadline_ms\":500,\"concurrency_limit\":1,\"children\":[{\"child_id\":\"a\",\"required\":true,\"delay_ms\":1,\"payload_bytes\":0,\"mode\":\"invented\"}]}")!=null)throw new AssertionError("invalid mode accepted");
    if(FanoutServer.parse("{\"request_id\":\"x\",\"deadline_ms\":500,\"concurrency_limit\":1,\"children\":[{\"child_id\":\"a\",\"required\":true,\"delay_ms\":1,\"payload_bytes\":0,\"extra\":true}]}")!=null)throw new AssertionError("unknown field accepted");
    var request=FanoutServer.parse("{\"request_id\":\"r1\",\"deadline_ms\":100,\"concurrency_limit\":2,\"children\":[{\"child_id\":\"a\",\"required\":true,\"delay_ms\":1,\"payload_bytes\":0}]}");
    String response=FanoutServer.run(request);if(!response.contains("\"runtime\":\"java\"")||!response.contains("\"active_tasks\":0"))throw new AssertionError(response);
    var deadline=FanoutServer.parse("{\"request_id\":\"r2\",\"deadline_ms\":50,\"concurrency_limit\":1,\"children\":[{\"child_id\":\"a\",\"required\":true,\"delay_ms\":40,\"payload_bytes\":0},{\"child_id\":\"b\",\"required\":true,\"delay_ms\":40,\"payload_bytes\":0}]}");
    String deadlineResponse=FanoutServer.run(deadline);if(!deadlineResponse.contains("\"child_id\":\"b\",\"status\":\"timeout\""))throw new AssertionError(deadlineResponse);
  }
}
